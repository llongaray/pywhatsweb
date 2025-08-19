"""
Gerenciador de sessões para PyWhatsWeb
"""

import os
import json
import qrcode
from typing import Optional, Dict, Any, Callable
from .exceptions import SessionError
from .database import DatabaseManager

class SessionManager:
    """Gerenciador de sessões do WhatsApp"""
    
    def __init__(self, database: DatabaseManager = None):
        """
        Inicializa o gerenciador de sessões
        
        Args:
            database: Instância do DatabaseManager
        """
        self.database = database or DatabaseManager()
        self.active_sessions = {}
        self.qr_callbacks = {}
        self.status_callbacks = {}
    
    def create_session(self, session_id: str, phone_number: str = None) -> str:
        """
        Cria uma nova sessão
        
        Args:
            session_id: ID único da sessão
            phone_number: Número do telefone (opcional)
            
        Returns:
            ID da sessão criada
        """
        if session_id in self.active_sessions:
            raise SessionError(f"Sessão {session_id} já existe")
        
        session_data = {
            'session_id': session_id,
            'phone_number': phone_number,
            'status': 'created',
            'qr_code': None,
            'authenticated': False,
            'created_at': self._get_timestamp(),
            'updated_at': self._get_timestamp()
        }
        
        self.active_sessions[session_id] = session_data
        self.database.save_session(session_id, session_data)
        
        return session_id
    
    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Recupera dados de uma sessão
        
        Args:
            session_id: ID da sessão
            
        Returns:
            Dados da sessão ou None se não existir
        """
        # Primeiro tenta da memória
        if session_id in self.active_sessions:
            return self.active_sessions[session_id]
        
        # Se não estiver na memória, tenta do banco
        session_data = self.database.get_session(session_id)
        if session_data:
            self.active_sessions[session_id] = session_data
            return session_data
        
        return None
    
    def update_session(self, session_id: str, **kwargs) -> bool:
        """
        Atualiza dados de uma sessão
        
        Args:
            session_id: ID da sessão
            **kwargs: Dados para atualizar
            
        Returns:
            True se atualizado com sucesso
        """
        if session_id not in self.active_sessions:
            raise SessionError(f"Sessão {session_id} não existe")
        
        session_data = self.active_sessions[session_id]
        session_data.update(kwargs)
        session_data['updated_at'] = self._get_timestamp()
        
        # Salva no banco
        self.database.save_session(session_id, session_data)
        
        return True
    
    def delete_session(self, session_id: str) -> bool:
        """
        Remove uma sessão
        
        Args:
            session_id: ID da sessão
            
        Returns:
            True se removida com sucesso
        """
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
        
        return self.database.delete_session(session_id)
    
    def list_sessions(self) -> list:
        """
        Lista todas as sessões
        
        Returns:
            Lista de IDs das sessões
        """
        return self.database.list_sessions()
    
    def set_qr_callback(self, session_id: str, callback: Callable):
        """
        Define callback para quando QR code for gerado
        
        Args:
            session_id: ID da sessão
            callback: Função callback
        """
        self.qr_callbacks[session_id] = callback
    
    def set_status_callback(self, session_id: str, callback: Callable):
        """
        Define callback para mudanças de status
        
        Args:
            session_id: ID da sessão
            callback: Função callback
        """
        self.status_callbacks[session_id] = callback
    
    def generate_qr(self, session_id: str) -> str:
        """
        Gera QR code para uma sessão
        
        Args:
            session_id: ID da sessão
            
        Returns:
            Caminho para o arquivo do QR code
        """
        if session_id not in self.active_sessions:
            raise SessionError(f"Sessão {session_id} não existe")
        
        # Gera QR code único para a sessão
        qr_data = f"whatsapp://session/{session_id}"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        # Cria diretório para QR codes se não existir
        qr_dir = os.path.join(os.path.expanduser("~"), ".pywhatsweb", "qr_codes")
        os.makedirs(qr_dir, exist_ok=True)
        
        # Salva QR code como imagem
        qr_path = os.path.join(qr_dir, f"{session_id}_qr.png")
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_path)
        
        # Atualiza sessão com caminho do QR
        self.update_session(session_id, qr_code=qr_path, status='qr_generated')
        
        # Executa callback se definido
        if session_id in self.qr_callbacks:
            try:
                self.qr_callbacks[session_id](qr_path)
            except Exception as e:
                print(f"Erro no callback do QR: {e}")
        
        return qr_path
    
    def authenticate_session(self, session_id: str, phone_number: str = None) -> bool:
        """
        Marca sessão como autenticada
        
        Args:
            session_id: ID da sessão
            phone_number: Número do telefone (opcional)
            
        Returns:
            True se autenticada com sucesso
        """
        if session_id not in self.active_sessions:
            raise SessionError(f"Sessão {session_id} não existe")
        
        update_data = {
            'status': 'authenticated',
            'authenticated': True,
            'phone_number': phone_number
        }
        
        if phone_number:
            update_data['phone_number'] = phone_number
        
        self.update_session(session_id, **update_data)
        
        # Executa callback de status se definido
        if session_id in self.status_callbacks:
            try:
                self.status_callbacks[session_id]('authenticated')
            except Exception as e:
                print(f"Erro no callback de status: {e}")
        
        return True
    
    def set_session_status(self, session_id: str, status: str) -> bool:
        """
        Define status de uma sessão
        
        Args:
            session_id: ID da sessão
            status: Novo status
            
        Returns:
            True se atualizado com sucesso
        """
        return self.update_session(session_id, status=status)
    
    def is_authenticated(self, session_id: str) -> bool:
        """
        Verifica se uma sessão está autenticada
        
        Args:
            session_id: ID da sessão
            
        Returns:
            True se autenticada
        """
        session = self.get_session(session_id)
        return session and session.get('authenticated', False)
    
    def get_session_status(self, session_id: str) -> Optional[str]:
        """
        Obtém status de uma sessão
        
        Args:
            session_id: ID da sessão
            
        Returns:
            Status da sessão ou None
        """
        session = self.get_session(session_id)
        return session.get('status') if session else None
    
    def _get_timestamp(self) -> str:
        """Retorna timestamp atual"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def close(self):
        """Fecha o gerenciador de sessões"""
        if self.database:
            self.database.close()
