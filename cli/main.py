"""
CLI principal para PyWhatsWeb
"""

import argparse
import sys
import os
from typing import Optional

# Adiciona o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.client import WhatsAppClient
from core.database import DatabaseManager
from utils.helpers import validate_phone_number, format_phone_number, generate_session_id

def main():
    """Função principal do CLI"""
    parser = argparse.ArgumentParser(
        description="PyWhatsWeb - Cliente WhatsApp para Python",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  pywhatsweb --session minha_sessao --connect
  pywhatsweb --session minha_sessao --send "5511999999999" "Olá, tudo bem?"
  pywhatsweb --session minha_sessao --send-image "5511999999999" "caminho/imagem.jpg"
  pywhatsweb --session minha_sessao --status
        """
    )
    
    # Argumentos principais
    parser.add_argument(
        '--session', '-s',
        type=str,
        help='ID da sessão (se não informado, será gerado automaticamente)'
    )
    
    parser.add_argument(
        '--database', '-d',
        type=str,
        choices=['localhost', 'sqlite', 'mysql'],
        default='localhost',
        help='Tipo de banco de dados (padrão: localhost)'
    )
    
    # Argumentos específicos do banco
    parser.add_argument(
        '--db-path',
        type=str,
        help='Caminho do arquivo SQLite (para --database sqlite)'
    )
    
    parser.add_argument(
        '--db-host',
        type=str,
        help='Host do MySQL (para --database mysql)'
    )
    
    parser.add_argument(
        '--db-user',
        type=str,
        help='Usuário do MySQL (para --database mysql)'
    )
    
    parser.add_argument(
        '--db-password',
        type=str,
        help='Senha do MySQL (para --database mysql)'
    )
    
    parser.add_argument(
        '--db-name',
        type=str,
        help='Nome do banco MySQL (para --database mysql)'
    )
    
    parser.add_argument(
        '--db-port',
        type=int,
        default=3306,
        help='Porta do MySQL (padrão: 3306)'
    )
    
    # Comandos
    parser.add_argument(
        '--connect',
        action='store_true',
        help='Conecta ao WhatsApp'
    )
    
    parser.add_argument(
        '--send',
        nargs=2,
        metavar=('NUMBER', 'MESSAGE'),
        help='Envia mensagem de texto'
    )
    
    parser.add_argument(
        '--send-image',
        nargs=2,
        metavar=('NUMBER', 'IMAGE_PATH'),
        help='Envia imagem'
    )
    
    parser.add_argument(
        '--send-document',
        nargs=2,
        metavar=('NUMBER', 'DOCUMENT_PATH'),
        help='Envia documento'
    )
    
    parser.add_argument(
        '--chats',
        action='store_true',
        help='Lista chats'
    )
    
    parser.add_argument(
        '--messages',
        type=str,
        metavar='CHAT_ID',
        help='Lista mensagens de um chat'
    )
    
    parser.add_argument(
        '--status',
        action='store_true',
        help='Mostra status da sessão'
    )
    
    parser.add_argument(
        '--disconnect',
        action='store_true',
        help='Desconecta do WhatsApp'
    )
    
    parser.add_argument(
        '--delete-session',
        action='store_true',
        help='Remove a sessão'
    )
    
    parser.add_argument(
        '--list-sessions',
        action='store_true',
        help='Lista todas as sessões'
    )
    
    # Argumentos de configuração
    parser.add_argument(
        '--wait-auth',
        type=int,
        default=300,
        help='Timeout para autenticação em segundos (padrão: 300)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Modo verboso'
    )
    
    args = parser.parse_args()
    
    # Se não há comandos, mostra ajuda
    if not any([
        args.connect, args.send, args.send_image, args.send_document,
        args.chats, args.messages, args.status, args.disconnect,
        args.delete_session, args.list_sessions
    ]):
        parser.print_help()
        return
    
    try:
        # Inicializa banco de dados
        db_kwargs = {}
        if args.database == 'sqlite':
            db_kwargs['db_path'] = args.db_path or 'whatsapp_sessions.db'
        elif args.database == 'mysql':
            if not all([args.db_host, args.db_user, args.db_password, args.db_name]):
                print("Erro: Para MySQL, informe --db-host, --db-user, --db-password e --db-name")
                return
            db_kwargs.update({
                'host': args.db_host,
                'user': args.db_user,
                'password': args.db_password,
                'database': args.db_name,
                'port': args.db_port
            })
        
        database = DatabaseManager(args.database, **db_kwargs)
        
        # Gera ou usa sessão existente
        session_id = args.session or generate_session_id()
        
        if args.verbose:
            print(f"Usando sessão: {session_id}")
            print(f"Tipo de banco: {args.database}")
        
        # Inicializa cliente
        client = WhatsAppClient(session_id, database)
        
        # Executa comandos
        if args.connect:
            print(f"Conectando ao WhatsApp...")
            if client.connect():
                print("Aguardando autenticação...")
                if client.wait_for_authentication(args.wait_auth):
                    print("Conectado e autenticado!")
                else:
                    print("Falha na autenticação")
        
        elif args.send:
            number, message = args.send
            if not validate_phone_number(number):
                print(f"Erro: Número inválido: {number}")
                return
            
            formatted_number = format_phone_number(number)
            print(f"Enviando mensagem para {formatted_number}...")
            
            if client.send_message(formatted_number, message):
                print("Mensagem enviada com sucesso!")
            else:
                print("Erro ao enviar mensagem")
        
        elif args.send_image:
            number, image_path = args.send_image
            if not validate_phone_number(number):
                print(f"Erro: Número inválido: {number}")
                return
            
            if not os.path.exists(image_path):
                print(f"Erro: Arquivo não encontrado: {image_path}")
                return
            
            formatted_number = format_phone_number(number)
            print(f"Enviando imagem para {formatted_number}...")
            
            if client.send_image(formatted_number, image_path):
                print("Imagem enviada com sucesso!")
            else:
                print("Erro ao enviar imagem")
        
        elif args.send_document:
            number, doc_path = args.send_document
            if not validate_phone_number(number):
                print(f"Erro: Número inválido: {number}")
                return
            
            if not os.path.exists(doc_path):
                print(f"Erro: Arquivo não encontrado: {doc_path}")
                return
            
            formatted_number = format_phone_number(number)
            print(f"Enviando documento para {formatted_number}...")
            
            if client.send_document(formatted_number, doc_path):
                print("Documento enviado com sucesso!")
            else:
                print("Erro ao enviar documento")
        
        elif args.chats:
            print("Listando chats...")
            chats = client.get_chats()
            for chat in chats:
                print(f"ID: {chat['id']}")
                print(f"Nome: {chat['name']}")
                print(f"Número: {chat['number']}")
                print(f"Última mensagem: {chat['last_message']}")
                print("-" * 30)
        
        elif args.messages:
            chat_id = args.messages
            print(f"Listando mensagens do chat {chat_id}...")
            messages = client.get_messages(chat_id)
            for msg in messages:
                print(f"De: {msg['from']}")
                print(f"Para: {msg['to']}")
                print(f"Conteúdo: {msg['content']}")
                print(f"Tipo: {msg['type']}")
                print(f"Status: {msg['status']}")
                print("-" * 30)
        
        elif args.status:
            status = client.get_status()
            print(f"Status da sessão {status['session_id']}:")
            print(f"Conectado: {status['connected']}")
            print(f"Autenticado: {status['authenticated']}")
            print(f"Status: {status['status']}")
            print(f"Telefone: {status['phone_number']}")
        
        elif args.disconnect:
            print("Desconectando...")
            client.disconnect()
            print("Desconectado!")
        
        elif args.delete_session:
            print(f"Removendo sessão {session_id}...")
            if client.session_manager.delete_session(session_id):
                print("Sessão removida!")
            else:
                print("Erro ao remover sessão")
        
        elif args.list_sessions:
            print("Sessões disponíveis:")
            sessions = database.list_sessions()
            for session in sessions:
                print(f"- {session}")
        
        # Fecha cliente
        client.close()
        
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário")
    except Exception as e:
        print(f"Erro: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
