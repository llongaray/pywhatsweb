# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Adicionado
- Estrutura inicial da biblioteca
- Cliente WhatsApp com Selenium
- Sistema de eventos e callbacks
- Suporte a envio de mensagens de texto
- Suporte a envio de mídia e documentos
- Suporte a envio de localização
- Criação e gerenciamento de grupos
- Sistema de configuração flexível
- Interface de linha de comando (CLI)
- Sistema de exceções personalizadas
- Modelos de dados estruturados
- Testes unitários abrangentes
- Configuração de CI/CD com GitHub Actions
- Suporte a Docker e Docker Compose
- Ferramentas de qualidade de código (Black, isort, flake8, mypy)
- Pre-commit hooks
- Documentação completa com exemplos
- Suporte a múltiplas versões do Python (3.8+)

### Mudado
- N/A

### Deprecado
- N/A

### Removido
- N/A

### Corrigido
- N/A

### Segurança
- N/A

## [0.1.0] - 2024-12-19

### Adicionado
- Lançamento inicial da biblioteca PyWhatsWeb
- Funcionalidades básicas de automação do WhatsApp Web
- Documentação completa e exemplos de uso
- Estrutura de projeto profissional
- Configuração para publicação no PyPI

---

## Notas de Versão

### Versão 0.1.0
Esta é a versão inicial da biblioteca PyWhatsWeb, fornecendo funcionalidades básicas de automação do WhatsApp Web usando Python e Selenium.

**Funcionalidades principais:**
- Conexão ao WhatsApp Web via QR Code
- Envio de mensagens de texto, mídia e documentos
- Criação e gerenciamento de grupos
- Sistema de eventos para mensagens recebidas
- Interface de linha de comando
- Configuração flexível via arquivo .env ou código

**Requisitos:**
- Python 3.8+
- Google Chrome
- ChromeDriver (gerenciado automaticamente)

**Instalação:**
```bash
pip install pywhatsweb
```

**Uso básico:**
```python
from pywhatsweb import WhatsAppClient

client = WhatsAppClient()
client.connect()
client.wait_for_qr()
client.wait_for_connection()
client.send_message("5511999999999", "Olá!")
client.disconnect()
```

---

## Como Contribuir

Para contribuir com este projeto, consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
