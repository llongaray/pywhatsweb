"""
Exemplo de integração do PyWhatsWeb com Flask
"""

from flask import Flask, request, jsonify, render_template_string
from pywhatsweb import WhatsAppClient, DatabaseManager
import json

app = Flask(__name__)

# Configuração do banco de dados
database = DatabaseManager("localhost")  # Pode ser alterado para sqlite ou mysql

# Cliente WhatsApp global
whatsapp_client = None

# Template HTML simples
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>PyWhatsWeb - Flask Integration</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
        .status { padding: 10px; margin: 10px 0; border-radius: 5px; }
        .status.connected { background-color: #d4edda; border: 1px solid #c3e6cb; }
        .status.disconnected { background-color: #f8d7da; border: 1px solid #f5c6cb; }
        .form-group { margin: 15px 0; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea, button { width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { background-color: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        button:disabled { background-color: #6c757d; cursor: not-allowed; }
        .qr-code { text-align: center; margin: 20px 0; }
        .qr-code img { max-width: 300px; border: 1px solid #ddd; }
        .messages { margin: 20px 0; }
        .message { padding: 10px; margin: 5px 0; background-color: #f8f9fa; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>PyWhatsWeb - Flask Integration</h1>
        
        <div class="status {{ 'connected' if status.connected else 'disconnected' }}">
            <strong>Status:</strong> {{ status.status }} | 
            <strong>Conectado:</strong> {{ 'Sim' if status.connected else 'Não' }} | 
            <strong>Autenticado:</strong> {{ 'Sim' if status.authenticated else 'Não' }}
        </div>
        
        <div class="form-group">
            <label>ID da Sessão:</label>
            <input type="text" id="session_id" value="{{ session_id }}" placeholder="Digite o ID da sessão">
        </div>
        
        <div class="form-group">
            <button onclick="connect()" {{ 'disabled' if status.connected else '' }}>Conectar</button>
            <button onclick="disconnect()" {{ 'disabled' if not status.connected else '' }}>Desconectar</button>
        </div>
        
        {% if qr_code %}
        <div class="qr-code">
            <h3>QR Code para Autenticação</h3>
            <img src="{{ qr_code }}" alt="QR Code">
            <p>Escaneie este QR code com seu WhatsApp</p>
        </div>
        {% endif %}
        
        <div class="form-group">
            <label>Número de Destino:</label>
            <input type="text" id="phone_number" placeholder="Ex: 5511999999999">
        </div>
        
        <div class="form-group">
            <label>Mensagem:</label>
            <textarea id="message" rows="4" placeholder="Digite sua mensagem"></textarea>
        </div>
        
        <div class="form-group">
            <button onclick="sendMessage()" {{ 'disabled' if not status.authenticated else '' }}>Enviar Mensagem</button>
        </div>
        
        <div class="form-group">
            <label>Arquivo (Imagem/Documento):</label>
            <input type="file" id="file_input">
            <button onclick="sendFile()" {{ 'disabled' if not status.authenticated else '' }}>Enviar Arquivo</button>
        </div>
        
        <div class="form-group">
            <button onclick="getChats()" {{ 'disabled' if not status.authenticated else '' }}>Listar Chats</button>
        </div>
        
        <div id="chats" class="messages"></div>
        
        <div class="form-group">
            <button onclick="deleteSession()">Deletar Sessão</button>
        </div>
    </div>
    
    <script>
        function connect() {
            const sessionId = document.getElementById('session_id').value;
            if (!sessionId) {
                alert('Digite um ID de sessão');
                return;
            }
            
            fetch('/connect', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({session_id: sessionId})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    alert('Erro: ' + data.message);
                }
            });
        }
        
        function disconnect() {
            fetch('/disconnect', {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();
                }
            });
        }
        
        function sendMessage() {
            const phone = document.getElementById('phone_number').value;
            const message = document.getElementById('message').value;
            
            if (!phone || !message) {
                alert('Preencha todos os campos');
                return;
            }
            
            fetch('/send_message', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({phone: phone, message: message})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Mensagem enviada!');
                    document.getElementById('message').value = '';
                } else {
                    alert('Erro: ' + data.message);
                }
            });
        }
        
        function sendFile() {
            const phone = document.getElementById('phone_number').value;
            const fileInput = document.getElementById('file_input');
            const file = fileInput.files[0];
            
            if (!phone || !file) {
                alert('Selecione um arquivo e digite o número');
                return;
            }
            
            const formData = new FormData();
            formData.append('phone', phone);
            formData.append('file', file);
            
            fetch('/send_file', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Arquivo enviado!');
                    fileInput.value = '';
                } else {
                    alert('Erro: ' + data.message);
                }
            });
        }
        
        function getChats() {
            fetch('/get_chats')
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const chatsDiv = document.getElementById('chats');
                    chatsDiv.innerHTML = '<h3>Chats Disponíveis</h3>';
                    
                    data.chats.forEach(chat => {
                        const chatDiv = document.createElement('div');
                        chatDiv.className = 'message';
                        chatDiv.innerHTML = `
                            <strong>${chat.name}</strong><br>
                            Número: ${chat.number}<br>
                            Última mensagem: ${chat.last_message}
                        `;
                        chatsDiv.appendChild(chatDiv);
                    });
                }
            });
        }
        
        function deleteSession() {
            if (confirm('Tem certeza que deseja deletar a sessão?')) {
                fetch('/delete_session', {method: 'POST'})
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        location.reload();
                    }
                });
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Página principal"""
    global whatsapp_client
    
    status = {
        'connected': False,
        'authenticated': False,
        'status': 'disconnected'
    }
    
    session_id = "minha_sessao"
    qr_code = None
    
    if whatsapp_client:
        try:
            status = whatsapp_client.get_status()
            session_id = whatsapp_client.session_id
            
            # Verifica se há QR code
            session_data = whatsapp_client.session_manager.get_session(session_id)
            if session_data and session_data.get('qr_code'):
                qr_code = session_data['qr_code']
        except:
            pass
    
    return render_template_string(HTML_TEMPLATE, 
                                status=status, 
                                session_id=session_id,
                                qr_code=qr_code)

@app.route('/connect', methods=['POST'])
def connect():
    """Conecta ao WhatsApp"""
    global whatsapp_client
    
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'minha_sessao')
        
        # Cria novo cliente
        whatsapp_client = WhatsAppClient(session_id, database)
        
        # Conecta
        if whatsapp_client.connect():
            return jsonify({'success': True, 'message': 'Conectado com sucesso'})
        else:
            return jsonify({'success': False, 'message': 'Erro ao conectar'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/disconnect', methods=['POST'])
def disconnect():
    """Desconecta do WhatsApp"""
    global whatsapp_client
    
    try:
        if whatsapp_client:
            whatsapp_client.disconnect()
            whatsapp_client = None
        
        return jsonify({'success': True, 'message': 'Desconectado com sucesso'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/send_message', methods=['POST'])
def send_message():
    """Envia mensagem de texto"""
    global whatsapp_client
    
    try:
        if not whatsapp_client or not whatsapp_client.authenticated:
            return jsonify({'success': False, 'message': 'Cliente não autenticado'})
        
        data = request.get_json()
        phone = data.get('phone')
        message = data.get('message')
        
        if not phone or not message:
            return jsonify({'success': False, 'message': 'Dados incompletos'})
        
        # Envia mensagem
        message_id = whatsapp_client.send_message(phone, message)
        
        return jsonify({'success': True, 'message': 'Mensagem enviada', 'message_id': message_id})
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/send_file', methods=['POST'])
def send_file():
    """Envia arquivo (imagem/documento)"""
    global whatsapp_client
    
    try:
        if not whatsapp_client or not whatsapp_client.authenticated:
            return jsonify({'success': False, 'message': 'Cliente não autenticado'})
        
        phone = request.form.get('phone')
        file = request.files.get('file')
        
        if not phone or not file:
            return jsonify({'success': False, 'message': 'Dados incompletos'})
        
        # Salva arquivo temporariamente
        import tempfile
        import os
        
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, file.filename)
        file.save(file_path)
        
        # Determina tipo de arquivo
        file_ext = os.path.splitext(file.filename)[1].lower()
        image_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        
        if file_ext in image_exts:
            message_id = whatsapp_client.send_image(phone, file_path, "Arquivo enviado via Flask")
        else:
            message_id = whatsapp_client.send_document(phone, file_path, "Documento enviado via Flask")
        
        # Remove arquivo temporário
        os.remove(file_path)
        os.rmdir(temp_dir)
        
        return jsonify({'success': True, 'message': 'Arquivo enviado', 'message_id': message_id})
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/get_chats')
def get_chats():
    """Obtém lista de chats"""
    global whatsapp_client
    
    try:
        if not whatsapp_client or not whatsapp_client.authenticated:
            return jsonify({'success': False, 'message': 'Cliente não autenticado'})
        
        chats = whatsapp_client.get_chats()
        return jsonify({'success': True, 'chats': chats})
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/delete_session', methods=['POST'])
def delete_session():
    """Deleta a sessão atual"""
    global whatsapp_client
    
    try:
        if whatsapp_client:
            session_id = whatsapp_client.session_id
            whatsapp_client.session_manager.delete_session(session_id)
            whatsapp_client = None
        
        return jsonify({'success': True, 'message': 'Sessão deletada'})
        
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/status')
def status():
    """Retorna status atual"""
    global whatsapp_client
    
    try:
        if whatsapp_client:
            return jsonify(whatsapp_client.get_status())
        else:
            return jsonify({
                'session_id': None,
                'connected': False,
                'authenticated': False,
                'status': 'disconnected',
                'phone_number': None
            })
            
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    print("Iniciando servidor Flask...")
    print("Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
