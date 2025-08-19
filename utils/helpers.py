"""
Funções utilitárias para PyWhatsWeb
"""

import re
import os
from typing import Optional, Dict, Any

def validate_phone_number(phone: str) -> bool:
    """
    Valida formato de número de telefone
    
    Args:
        phone: Número do telefone
        
    Returns:
        True se válido
    """
    # Remove caracteres especiais
    phone = re.sub(r'[^\d+]', '', phone)
    
    # Verifica se tem pelo menos 10 dígitos
    if len(phone) < 10:
        return False
    
    # Verifica se começa com + ou código do país
    if not (phone.startswith('+') or phone.startswith('55')):
        return False
    
    return True

def format_phone_number(phone: str) -> str:
    """
    Formata número de telefone para padrão internacional
    
    Args:
        phone: Número do telefone
        
    Returns:
        Número formatado
    """
    # Remove caracteres especiais
    phone = re.sub(r'[^\d+]', '', phone)
    
    # Adiciona + se não tiver
    if not phone.startswith('+'):
        if phone.startswith('55'):
            phone = '+' + phone
        else:
            phone = '+55' + phone
    
    return phone

def sanitize_filename(filename: str) -> str:
    """
    Sanitiza nome de arquivo para uso seguro
    
    Args:
        filename: Nome do arquivo
        
    Returns:
        Nome sanitizado
    """
    # Remove caracteres inválidos
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    
    # Remove espaços extras
    filename = re.sub(r'\s+', '_', filename)
    
    # Remove caracteres especiais
    filename = re.sub(r'[^\w\-_.]', '', filename)
    
    return filename

def create_directory(path: str) -> bool:
    """
    Cria diretório se não existir
    
    Args:
        path: Caminho do diretório
        
    Returns:
        True se criado com sucesso
    """
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception:
        return False

def get_file_size(file_path: str) -> Optional[int]:
    """
    Obtém tamanho de arquivo em bytes
    
    Args:
        file_path: Caminho do arquivo
        
    Returns:
        Tamanho em bytes ou None se erro
    """
    try:
        return os.path.getsize(file_path)
    except Exception:
        return None

def is_valid_file(file_path: str, allowed_extensions: list = None) -> bool:
    """
    Verifica se arquivo é válido
    
    Args:
        file_path: Caminho do arquivo
        allowed_extensions: Lista de extensões permitidas
        
    Returns:
        True se válido
    """
    if not os.path.exists(file_path):
        return False
    
    if not os.path.isfile(file_path):
        return False
    
    if allowed_extensions:
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext not in allowed_extensions:
            return False
    
    return True

def generate_session_id(prefix: str = "session") -> str:
    """
    Gera ID único para sessão
    
    Args:
        prefix: Prefixo para o ID
        
    Returns:
        ID único da sessão
    """
    import time
    import random
    
    timestamp = int(time.time() * 1000)
    random_suffix = random.randint(1000, 9999)
    
    return f"{prefix}_{timestamp}_{random_suffix}"

def parse_message_content(content: str, max_length: int = 4096) -> str:
    """
    Parse e valida conteúdo de mensagem
    
    Args:
        content: Conteúdo da mensagem
        max_length: Tamanho máximo permitido
        
    Returns:
        Conteúdo validado
    """
    if not content:
        return ""
    
    # Remove caracteres de controle
    content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', content)
    
    # Limita tamanho
    if len(content) > max_length:
        content = content[:max_length-3] + "..."
    
    return content.strip()

def create_config_file(config_path: str, config_data: Dict[str, Any]) -> bool:
    """
    Cria arquivo de configuração
    
    Args:
        config_path: Caminho do arquivo
        config_data: Dados da configuração
        
    Returns:
        True se criado com sucesso
    """
    try:
        import json
        
        # Cria diretório se não existir
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception:
        return False

def load_config_file(config_path: str) -> Optional[Dict[str, Any]]:
    """
    Carrega arquivo de configuração
    
    Args:
        config_path: Caminho do arquivo
        
    Returns:
        Dados da configuração ou None se erro
    """
    try:
        import json
        
        if not os.path.exists(config_path):
            return None
        
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    except Exception:
        return None
