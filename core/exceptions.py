"""
Exceções customizadas para PyWhatsWeb
"""

class WhatsAppError(Exception):
    """Exceção base para erros do WhatsApp"""
    pass

class SessionError(WhatsAppError):
    """Erro relacionado ao gerenciamento de sessões"""
    pass

class DatabaseError(WhatsAppError):
    """Erro relacionado ao banco de dados"""
    pass

class ConnectionError(WhatsAppError):
    """Erro de conexão com WhatsApp Web"""
    pass

class AuthenticationError(WhatsAppError):
    """Erro de autenticação"""
    pass

class MessageError(WhatsAppError):
    """Erro relacionado ao envio/recebimento de mensagens"""
    pass
