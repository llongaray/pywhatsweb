"""
Exemplo básico de uso do PyWhatsWeb
"""

from pywhatsweb import WhatsAppClient, DatabaseManager

def exemplo_basico():
    """Exemplo básico de uso"""
    
    # Inicializa banco de dados (localhost por padrão)
    database = DatabaseManager()
    
    # Cria cliente com sessão
    client = WhatsAppClient("minha_sessao", database)
    
    try:
        # Conecta ao WhatsApp
        print("Conectando ao WhatsApp...")
        if client.connect():
            print("QR Code gerado! Escaneie com seu WhatsApp")
            
            # Aguarda autenticação
            print("Aguardando autenticação...")
            if client.wait_for_authentication(timeout=300):
                print("Autenticado com sucesso!")
                
                # Envia mensagem
                numero = "5511999999999"  # Substitua pelo número real
                mensagem = "Olá! Esta é uma mensagem de teste do PyWhatsWeb!"
                
                print(f"Enviando mensagem para {numero}...")
                message_id = client.send_message(numero, mensagem)
                print(f"Mensagem enviada! ID: {message_id}")
                
                # Lista chats
                print("\nChats disponíveis:")
                chats = client.get_chats()
                for chat in chats:
                    print(f"- {chat['name']} ({chat['number']})")
                
            else:
                print("Falha na autenticação")
        else:
            print("Erro ao conectar")
            
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        # Sempre fecha o cliente
        client.close()

def exemplo_com_sqlite():
    """Exemplo usando SQLite como banco"""
    
    # Inicializa banco SQLite
    database = DatabaseManager("sqlite", db_path="whatsapp.db")
    
    # Cria cliente
    client = WhatsAppClient("sessao_sqlite", database)
    
    try:
        # Conecta
        if client.connect():
            print("Conectado via SQLite!")
            
            # Aguarda autenticação
            if client.wait_for_authentication():
                print("Autenticado!")
                
                # Envia imagem
                numero = "5511999999999"
                imagem = "caminho/para/imagem.jpg"
                
                print("Enviando imagem...")
                message_id = client.send_image(numero, imagem, "Imagem de teste!")
                print(f"Imagem enviada! ID: {message_id}")
                
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        client.close()

def exemplo_com_mysql():
    """Exemplo usando MySQL como banco"""
    
    # Inicializa banco MySQL
    database = DatabaseManager(
        "mysql",
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="whatsapp_db",
        port=3306
    )
    
    # Cria cliente
    client = WhatsAppClient("sessao_mysql", database)
    
    try:
        # Conecta
        if client.connect():
            print("Conectado via MySQL!")
            
            # Aguarda autenticação
            if client.wait_for_authentication():
                print("Autenticado!")
                
                # Envia documento
                numero = "5511999999999"
                documento = "caminho/para/documento.pdf"
                
                print("Enviando documento...")
                message_id = client.send_document(numero, documento, "Documento de teste!")
                print(f"Documento enviado! ID: {message_id}")
                
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        client.close()

def exemplo_com_callbacks():
    """Exemplo usando callbacks"""
    
    database = DatabaseManager()
    client = WhatsAppClient("sessao_callbacks", database)
    
    # Define callbacks
    def on_message_received(message_data):
        print(f"Nova mensagem recebida: {message_data}")
    
    def on_status_changed(status):
        print(f"Status mudou para: {status}")
    
    client.set_message_callback(on_message_received)
    client.set_status_callback(on_status_changed)
    
    try:
        if client.connect():
            print("Conectado!")
            
            if client.wait_for_authentication():
                print("Autenticado!")
                
                # Simula recebimento de mensagem
                print("Simulando recebimento de mensagem...")
                # Aqui você implementaria a lógica real de recebimento
                
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    print("=== Exemplo Básico ===")
    exemplo_basico()
    
    print("\n=== Exemplo com SQLite ===")
    exemplo_com_sqlite()
    
    print("\n=== Exemplo com MySQL ===")
    exemplo_com_mysql()
    
    print("\n=== Exemplo com Callbacks ===")
    exemplo_com_callbacks()
