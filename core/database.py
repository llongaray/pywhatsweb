"""
Gerenciador de banco de dados para PyWhatsWeb
Suporta SQLite, MySQL e armazenamento local
"""

import sqlite3
import json
import os
from typing import Optional, Dict, Any, List
from .exceptions import DatabaseError

class DatabaseManager:
    """Gerenciador de banco de dados para sessões e dados do WhatsApp"""
    
    def __init__(self, db_type: str = "localhost", **kwargs):
        """
        Inicializa o gerenciador de banco
        
        Args:
            db_type: Tipo de banco ('localhost', 'sqlite', 'mysql')
            **kwargs: Parâmetros específicos do banco
        """
        self.db_type = db_type
        self.connection = None
        self.cursor = None
        
        if db_type == "sqlite":
            self._init_sqlite(**kwargs)
        elif db_type == "mysql":
            self._init_mysql(**kwargs)
        elif db_type == "localhost":
            self._init_localhost(**kwargs)
        else:
            raise DatabaseError(f"Tipo de banco não suportado: {db_type}")
    
    def _init_sqlite(self, db_path: str = "whatsapp_sessions.db"):
        """Inicializa conexão SQLite"""
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
            self._create_tables()
        except Exception as e:
            raise DatabaseError(f"Erro ao conectar SQLite: {e}")
    
    def _init_mysql(self, host: str, user: str, password: str, database: str, port: int = 3306):
        """Inicializa conexão MySQL"""
        try:
            import mysql.connector
            self.connection = mysql.connector.connect(
                host=host, user=user, password=password, 
                database=database, port=port
            )
            self.cursor = self.connection.cursor()
            self._create_tables()
        except ImportError:
            raise DatabaseError("mysql-connector-python não instalado")
        except Exception as e:
            raise DatabaseError(f"Erro ao conectar MySQL: {e}")
    
    def _init_localhost(self, sessions_dir: str = None):
        """Inicializa armazenamento local"""
        if sessions_dir is None:
            sessions_dir = os.path.join(os.path.expanduser("~"), ".pywhatsweb", "sessions")
        
        self.sessions_dir = sessions_dir
        os.makedirs(sessions_dir, exist_ok=True)
    
    def _create_tables(self):
        """Cria tabelas necessárias"""
        if self.db_type in ["sqlite", "mysql"]:
            create_sessions_table = """
            CREATE TABLE IF NOT EXISTS whatsapp_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id VARCHAR(255) UNIQUE NOT NULL,
                phone_number VARCHAR(20),
                qr_code TEXT,
                status VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                session_data TEXT
            )
            """
            
            create_messages_table = """
            CREATE TABLE IF NOT EXISTS whatsapp_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id VARCHAR(255),
                message_id VARCHAR(255),
                from_number VARCHAR(20),
                to_number VARCHAR(20),
                message_type VARCHAR(50),
                content TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status VARCHAR(50),
                FOREIGN KEY (session_id) REFERENCES whatsapp_sessions(session_id)
            )
            """
            
            try:
                self.cursor.execute(create_sessions_table)
                self.cursor.execute(create_messages_table)
                self.connection.commit()
            except Exception as e:
                raise DatabaseError(f"Erro ao criar tabelas: {e}")
    
    def save_session(self, session_id: str, session_data: Dict[str, Any]) -> bool:
        """Salva dados da sessão"""
        try:
            if self.db_type == "localhost":
                return self._save_session_local(session_id, session_data)
            else:
                return self._save_session_db(session_id, session_data)
        except Exception as e:
            raise DatabaseError(f"Erro ao salvar sessão: {e}")
    
    def _save_session_local(self, session_id: str, session_data: Dict[str, Any]) -> bool:
        """Salva sessão localmente"""
        file_path = os.path.join(self.sessions_dir, f"{session_id}.json")
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False
    
    def _save_session_db(self, session_id: str, session_data: Dict[str, Any]) -> bool:
        """Salva sessão no banco de dados"""
        try:
            query = """
            INSERT OR REPLACE INTO whatsapp_sessions 
            (session_id, phone_number, qr_code, status, session_data, updated_at)
            VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """
            
            self.cursor.execute(query, (
                session_id,
                session_data.get('phone_number'),
                session_data.get('qr_code'),
                session_data.get('status'),
                json.dumps(session_data)
            ))
            
            self.connection.commit()
            return True
        except Exception:
            return False
    
    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Recupera dados da sessão"""
        try:
            if self.db_type == "localhost":
                return self._get_session_local(session_id)
            else:
                return self._get_session_db(session_id)
        except Exception as e:
            raise DatabaseError(f"Erro ao recuperar sessão: {e}")
    
    def _get_session_local(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Recupera sessão local"""
        file_path = os.path.join(self.sessions_dir, f"{session_id}.json")
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return None
        return None
    
    def _get_session_db(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Recupera sessão do banco"""
        try:
            query = "SELECT session_data FROM whatsapp_sessions WHERE session_id = ?"
            self.cursor.execute(query, (session_id,))
            result = self.cursor.fetchone()
            
            if result:
                return json.loads(result[0])
            return None
        except Exception:
            return None
    
    def delete_session(self, session_id: str) -> bool:
        """Remove uma sessão"""
        try:
            if self.db_type == "localhost":
                return self._delete_session_local(session_id)
            else:
                return self._delete_session_db(session_id)
        except Exception as e:
            raise DatabaseError(f"Erro ao deletar sessão: {e}")
    
    def _delete_session_local(self, session_id: str) -> bool:
        """Remove sessão local"""
        file_path = os.path.join(self.sessions_dir, f"{session_id}.json")
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            return True
        except Exception:
            return False
    
    def _delete_session_db(self, session_id: str) -> bool:
        """Remove sessão do banco"""
        try:
            query = "DELETE FROM whatsapp_sessions WHERE session_id = ?"
            self.cursor.execute(query, (session_id,))
            self.connection.commit()
            return True
        except Exception:
            return False
    
    def list_sessions(self) -> List[str]:
        """Lista todas as sessões"""
        try:
            if self.db_type == "localhost":
                return self._list_sessions_local()
            else:
                return self._list_sessions_db()
        except Exception as e:
            raise DatabaseError(f"Erro ao listar sessões: {e}")
    
    def _list_sessions_local(self) -> List[str]:
        """Lista sessões locais"""
        sessions = []
        for file_name in os.listdir(self.sessions_dir):
            if file_name.endswith('.json'):
                sessions.append(file_name.replace('.json', ''))
        return sessions
    
    def _list_sessions_db(self) -> List[str]:
        """Lista sessões do banco"""
        try:
            query = "SELECT session_id FROM whatsapp_sessions"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return [row[0] for row in results]
        except Exception:
            return []
    
    def close(self):
        """Fecha conexões do banco"""
        if self.connection:
            self.connection.close()
