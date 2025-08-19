"""
Cliente principal do WhatsApp para PyWhatsWeb
"""

import time
import json
from typing import Optional, Dict, Any, List, Callable
from .exceptions import WhatsAppError, ConnectionError, AuthenticationError, MessageError
from .session import SessionManager
from .database import DatabaseManager

class WhatsAppClient:
    """Cliente principal do WhatsApp"""
    
    def __init__(self, session_id: str, database: DatabaseManager = None):
        """
        Inicializa o cliente WhatsApp
        
        Args:
            session_id: ID da sessão
            database: Instância do DatabaseManager
        """
        self.session_id = session_id
        self.database = database or DatabaseManager()
        self.session_manager = SessionManager(database)
        self.connected = False
        self.authenticated = False
        self.message_callbacks = {}
        self.status_callbacks = {}
        
        # Verifica se a sessão existe, se não, cria
        if not self.session_manager.get_session(session_id):
            self.session_manager.create_session(session_id)
    
    def connect(self) -> bool:
        """
        Conecta ao WhatsApp Web
        
        Returns:
            True se conectado com sucesso
        """
        try:
            # Simula processo de conexão
            self.session_manager.set_session_status(self.session_id, 'connecting')
            
            # Gera QR code para autenticação
            qr_path = self.session_manager.generate_qr(self.session_id)
            
            self.session_manager.set_session_status(self.session_id, 'qr_ready')
            self.connected = True
            
            print(f"QR Code gerado: {qr_path}")
            print("Escaneie o QR code com seu WhatsApp")
            
            return True
            
        except Exception as e:
            self.session_manager.set_session_status(self.session_id, 'error')
            raise ConnectionError(f"Erro ao conectar: {e}")
    
    def wait_for_authentication(self, timeout: int = 300) -> bool:
        """
        Aguarda autenticação do usuário
        
        Args:
            timeout: Timeout em segundos
            
        Returns:
            True se autenticado com sucesso
        """
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if self.session_manager.is_authenticated(self.session_id):
                self.authenticated = True
                self.session_manager.set_session_status(self.session_id, 'ready')
                print("WhatsApp autenticado com sucesso!")
                return True
            
            time.sleep(2)
            print("Aguardando autenticação...")
        
        raise AuthenticationError("Timeout de autenticação")
    
    def send_message(self, to_number: str, message: str, message_type: str = "text") -> str:
        """
        Envia mensagem para um número
        
        Args:
            to_number: Número de destino
            message: Conteúdo da mensagem
            message_type: Tipo da mensagem (text, image, document, etc.)
            
        Returns:
            ID da mensagem enviada
        """
        if not self.authenticated:
            raise AuthenticationError("Cliente não autenticado")
        
        if not self.connected:
            raise ConnectionError("Cliente não conectado")
        
        try:
            # Simula envio de mensagem
            message_id = f"msg_{int(time.time())}_{self.session_id}"
            
            # Salva mensagem no banco
            self._save_message(message_id, to_number, message, message_type, "sent")
            
            # Simula delay de envio
            time.sleep(1)
            
            print(f"Mensagem enviada para {to_number}: {message}")
            return message_id
            
        except Exception as e:
            raise MessageError(f"Erro ao enviar mensagem: {e}")
    
    def send_image(self, to_number: str, image_path: str, caption: str = "") -> str:
        """
        Envia imagem para um número
        
        Args:
            to_number: Número de destino
            image_path: Caminho da imagem
            caption: Legenda da imagem
            
        Returns:
            ID da mensagem enviada
        """
        if not self.authenticated:
            raise AuthenticationError("Cliente não autenticado")
        
        try:
            message_id = f"img_{int(time.time())}_{self.session_id}"
            
            # Simula envio de imagem
            self._save_message(message_id, to_number, image_path, "image", "sent", caption)
            
            print(f"Imagem enviada para {to_number}: {image_path}")
            return message_id
            
        except Exception as e:
            raise MessageError(f"Erro ao enviar imagem: {e}")
    
    def send_document(self, to_number: str, document_path: str, caption: str = "") -> str:
        """
        Envia documento para um número
        
        Args:
            to_number: Número de destino
            document_path: Caminho do documento
            caption: Legenda do documento
            
        Returns:
            ID da mensagem enviada
        """
        if not self.authenticated:
            raise AuthenticationError("Cliente não autenticated")
        
        try:
            message_id = f"doc_{int(time.time())}_{self.session_id}"
            
            # Simula envio de documento
            self._save_message(message_id, to_number, document_path, "document", "sent", caption)
            
            print(f"Documento enviado para {to_number}: {document_path}")
            return message_id
            
        except Exception as e:
            raise MessageError(f"Erro ao enviar documento: {e}")
    
    def get_chats(self) -> List[Dict[str, Any]]:
        """
        Obtém lista de chats
        
        Returns:
            Lista de chats
        """
        if not self.authenticated:
            raise AuthenticationError("Cliente não autenticado")
        
        # Simula lista de chats
        chats = [
            {
                'id': 'chat_1',
                'name': 'Chat Teste 1',
                'number': '5511999999999',
                'last_message': 'Olá!',
                'timestamp': time.time()
            },
            {
                'id': 'chat_2', 
                'name': 'Chat Teste 2',
                'number': '5511888888888',
                'last_message': 'Tudo bem?',
                'timestamp': time.time() - 3600
            }
        ]
        
        return chats
    
    def get_messages(self, chat_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Obtém mensagens de um chat
        
        Args:
            chat_id: ID do chat
            limit: Limite de mensagens
            
        Returns:
            Lista de mensagens
        """
        if not self.authenticated:
            raise AuthenticationError("Cliente não autenticado")
        
        # Simula mensagens do chat
        messages = []
        for i in range(min(limit, 10)):
            messages.append({
                'id': f'msg_{i}',
                'from': '5511999999999',
                'to': '5511888888888',
                'content': f'Mensagem de teste {i}',
                'type': 'text',
                'timestamp': time.time() - (i * 60),
                'status': 'read'
            })
        
        return messages
    
    def set_message_callback(self, callback: Callable):
        """
        Define callback para mensagens recebidas
        
        Args:
            callback: Função callback
        """
        self.message_callbacks[self.session_id] = callback
    
    def set_status_callback(self, callback: Callable):
        """
        Define callback para mudanças de status
        
        Args:
            callback: Função callback
        """
        self.status_callbacks[self.session_id] = callback
    
    def disconnect(self):
        """Desconecta do WhatsApp"""
        self.connected = False
        self.authenticated = False
        self.session_manager.set_session_status(self.session_id, 'disconnected')
        print("Desconectado do WhatsApp")
    
    def get_status(self) -> Dict[str, Any]:
        """
        Obtém status atual do cliente
        
        Returns:
            Dicionário com status
        """
        session = self.session_manager.get_session(self.session_id)
        
        return {
            'session_id': self.session_id,
            'connected': self.connected,
            'authenticated': self.authenticated,
            'status': session.get('status') if session else 'unknown',
            'phone_number': session.get('phone_number') if session else None
        }
    
    def _save_message(self, message_id: str, to_number: str, content: str, 
                     message_type: str, status: str, caption: str = ""):
        """Salva mensagem no banco de dados"""
        try:
            if hasattr(self.database, 'save_message'):
                message_data = {
                    'message_id': message_id,
                    'session_id': self.session_id,
                    'from_number': None,  # Será preenchido quando implementar recebimento
                    'to_number': to_number,
                    'message_type': message_type,
                    'content': content,
                    'caption': caption,
                    'status': status
                }
                self.database.save_message(message_id, message_data)
        except Exception as e:
            print(f"Erro ao salvar mensagem: {e}")
    
    def close(self):
        """Fecha o cliente"""
        self.disconnect()
        if self.session_manager:
            self.session_manager.close()
        if self.database:
            self.database.close()
