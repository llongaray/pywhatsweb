"""
PyWhatsWeb - Biblioteca Python para WhatsApp Web
Baseada na funcionalidade do whatsapp-web.js
"""

__version__ = "1.0.0"
__author__ = "TI Léo Team"
__description__ = "Biblioteca Python para automação do WhatsApp Web"

from .core.client import WhatsAppClient
from .core.session import SessionManager
from .core.database import DatabaseManager
from .core.exceptions import WhatsAppError, SessionError, DatabaseError

__all__ = [
    "WhatsAppClient",
    "SessionManager", 
    "DatabaseManager",
    "WhatsAppError",
    "SessionError",
    "DatabaseError"
]
