# PyWhatsWeb 🚀

**Biblioteca Python para automação do WhatsApp Web** - Baseada na funcionalidade do `whatsapp-web.js`

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://pypi.org/project/pywhatsweb/)

## ✨ Características

- 🔐 **Autenticação via QR Code** - Conecte-se ao WhatsApp Web facilmente
- 💾 **Múltiplos bancos de dados** - Suporte a SQLite, MySQL e armazenamento local
- 📱 **Envio de mensagens** - Texto, imagens, documentos e mais
- 🎯 **CLI integrado** - Use direto do terminal
- 🌐 **Integração web** - Compatível com Flask e Django
- 🔄 **Gerenciamento de sessões** - Múltiplas sessões simultâneas
- 📊 **Callbacks e eventos** - Sistema de notificações em tempo real
- 🛡️ **Tratamento de erros** - Exceções customizadas e robustas

## 🚀 Instalação

### Via pip
```bash
pip install pywhatsweb
```

### Via source
```bash
git clone https://github.com/tileo/pywhatsweb.git
cd pywhatsweb
pip install -e .
```

### Dependências opcionais
```bash
# Para MySQL
pip install pywhatsweb[mysql]

# Para Flask
pip install pywhatsweb[flask]

# Para Django
pip install pywhatsweb[django]

# Para Celery
pip install pywhatsweb[celery]
```

## 📖 Uso Básico

### CLI (Terminal)
```bash
# Conectar ao WhatsApp
pywhatsweb --session minha_sessao --connect

# Enviar mensagem
pywhatsweb --session minha_sessao --send "5511999999999" "Olá, tudo bem?"

# Enviar imagem
pywhatsweb --session minha_sessao --send-image "5511999999999" "caminho/imagem.jpg"

# Ver status
pywhatsweb --session minha_sessao --status
```

### Python
```python
from pywhatsweb import WhatsAppClient, DatabaseManager

# Inicializa banco de dados
database = DatabaseManager("localhost")  # ou "sqlite", "mysql"

# Cria cliente
client = WhatsAppClient("minha_sessao", database)

# Conecta
if client.connect():
    print("QR Code gerado! Escaneie com seu WhatsApp")
    
    # Aguarda autenticação
    if client.wait_for_authentication():
        print("Autenticado!")
        
        # Envia mensagem
        message_id = client.send_message("5511999999999", "Olá!")
        print(f"Mensagem enviada: {message_id}")
        
        # Lista chats
        chats = client.get_chats()
        for chat in chats:
            print(f"- {chat['name']} ({chat['number']})")

# Sempre fecha o cliente
client.close()
```

## 🗄️ Configuração de Banco de Dados

### Localhost (padrão)
```python
database = DatabaseManager("localhost")
```

### SQLite
```python
database = DatabaseManager("sqlite", db_path="whatsapp.db")
```

### MySQL
```python
database = DatabaseManager(
    "mysql",
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="whatsapp_db",
    port=3306
)
```

## 🌐 Integração com Web Frameworks

### Flask
```python
from flask import Flask, request, jsonify
from pywhatsweb import WhatsAppClient, DatabaseManager

app = Flask(__name__)
database = DatabaseManager()
client = WhatsAppClient("web_session", database)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    phone = data.get('phone')
    message = data.get('message')
    
    message_id = client.send_message(phone, message)
    return jsonify({'success': True, 'message_id': message_id})

if __name__ == '__main__':
    app.run(debug=True)
```

### Django
```python
from django.http import JsonResponse
from pywhatsweb import WhatsAppClient, DatabaseManager

def send_message(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        database = DatabaseManager()
        client = WhatsAppClient("django_session", database)
        
        if client.connect() and client.wait_for_authentication():
            message_id = client.send_message(phone, message)
            client.close()
            return JsonResponse({'success': True, 'message_id': message_id})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})
```

## 🔧 Configuração Avançada

### Callbacks e Eventos
```python
def on_message_received(message_data):
    print(f"Nova mensagem: {message_data}")

def on_status_changed(status):
    print(f"Status mudou: {status}")

client.set_message_callback(on_message_received)
client.set_status_callback(on_status_changed)
```

### Múltiplas Sessões
```python
# Sessão 1
client1 = WhatsAppClient("sessao_1", database)
client1.connect()

# Sessão 2
client2 = WhatsAppClient("sessao_2", database)
client2.connect()

# Ambas funcionam independentemente
```

## 📁 Estrutura do Projeto

```
pywhatsweb/
├── core/                    # Funcionalidades principais
│   ├── client.py          # Cliente WhatsApp
│   ├── session.py         # Gerenciador de sessões
│   ├── database.py        # Gerenciador de banco
│   └── exceptions.py      # Exceções customizadas
├── utils/                  # Utilitários
│   └── helpers.py         # Funções auxiliares
├── cli/                    # Interface de linha de comando
│   └── main.py            # CLI principal
├── examples/               # Exemplos de uso
│   ├── basic_usage.py     # Uso básico
│   ├── flask_integration.py # Integração Flask
│   └── django_integration.py # Integração Django
├── setup.py               # Configuração de instalação
├── requirements.txt        # Dependências
└── README.md              # Este arquivo
```

## 🧪 Exemplos

Veja a pasta `examples/` para exemplos completos de:
- Uso básico da biblioteca
- Integração com Flask
- Integração com Django
- Uso com diferentes bancos de dados

## 🚨 Limitações

⚠️ **Importante**: Esta biblioteca é uma implementação educacional e de demonstração. Para uso em produção, considere:

- Implementar autenticação real com WhatsApp Web
- Adicionar validações de segurança
- Implementar rate limiting
- Adicionar logs e monitoramento
- Testar extensivamente

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⚠️ Disclaimer

Esta biblioteca é fornecida "como está", sem garantias de qualquer tipo. O uso desta biblioteca para automação do WhatsApp deve seguir os Termos de Serviço do WhatsApp e leis aplicáveis.

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/tileo/pywhatsweb/issues)
- **Documentação**: [README](https://github.com/tileo/pywhatsweb#readme)
- **Email**: ti.leo@example.com

---

**Desenvolvido com ❤️ pela TI Léo Team**
