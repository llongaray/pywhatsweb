# PyWhatsWeb

Uma biblioteca Python para automação do WhatsApp Web, inspirada no [whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js).

## 🚀 Características

- **Automação completa do WhatsApp Web** usando Selenium
- **Envio e recebimento de mensagens** (texto, mídia, documentos)
- **Gerenciamento de sessões** com QR Code
- **Eventos em tempo real** (mensagens recebidas, conexão, etc.)
- **API simples e intuitiva** para Python
- **Suporte a múltiplas instâncias**

## 📦 Instalação

```bash
pip install pywhatsweb
```

### Desenvolvimento

```bash
git clone https://github.com/llongaray/pywhatsweb.git
cd pywhatsweb
pip install -e .
```

## 🔧 Uso Básico

### Exemplo Simples

```python
from pywhatsweb import WhatsAppClient

# Criar cliente
client = WhatsAppClient()

# Conectar ao WhatsApp
client.connect()

# Aguardar QR Code
client.wait_for_qr()

# Enviar mensagem
client.send_message("5511999999999", "Olá! Teste da biblioteca PyWhatsWeb!")

# Fechar conexão
client.disconnect()
```

### Exemplo com Eventos

```python
from pywhatsweb import WhatsAppClient

def on_message_received(message):
    print(f"Mensagem recebida de {message.sender}: {message.content}")
    
    # Auto-resposta
    if "oi" in message.content.lower():
        client.send_message(message.sender, "Oi! Como posso ajudar?")

# Configurar cliente com eventos
client = WhatsAppClient()
client.on_message = on_message_received

# Conectar e aguardar
client.connect()
client.wait_for_qr()
client.wait_forever()
```

## 📱 Funcionalidades

### Mensagens

- **Texto**: `send_message(phone, text)`
- **Mídia**: `send_media(phone, file_path, caption="")`
- **Documentos**: `send_document(phone, file_path, caption="")`
- **Localização**: `send_location(phone, lat, lng, name="")`

### Grupos

- **Criar grupo**: `create_group(name, participants)`
- **Adicionar participantes**: `add_participants(group_id, participants)`
- **Remover participantes**: `remove_participants(group_id, participants)`
- **Enviar para grupo**: `send_message_to_group(group_id, message)`

### Eventos

- `on_message`: Mensagem recebida
- `on_connection`: Conexão estabelecida
- `on_disconnection`: Desconexão
- `on_qr`: QR Code gerado
- `on_ready`: Cliente pronto

## 🛠️ Configuração

### Variáveis de Ambiente

```bash
# .env
WHATSAPP_HEADLESS=false
WHATSAPP_TIMEOUT=30
WHATSAPP_USER_DATA_DIR=./whatsapp_data
```

### Configuração Avançada

```python
from pywhatsweb import WhatsAppClient, Config

config = Config(
    headless=False,
    timeout=30,
    user_data_dir="./whatsapp_data",
    chrome_options=["--no-sandbox", "--disable-dev-shm-usage"]
)

client = WhatsAppClient(config=config)
```

## 🧪 Testes

```bash
# Instalar dependências de desenvolvimento
pip install -e ".[dev]"

# Executar testes
pytest

# Com cobertura
pytest --cov=pywhatsweb
```

## 📚 API Reference

### WhatsAppClient

#### Métodos Principais

- `connect()`: Conecta ao WhatsApp Web
- `disconnect()`: Desconecta e fecha o navegador
- `wait_for_qr()`: Aguarda o QR Code ser escaneado
- `wait_forever()`: Mantém a conexão ativa
- `send_message(phone, text)`: Envia mensagem de texto
- `send_media(phone, file_path, caption="")`: Envia mídia
- `send_document(phone, file_path, caption="")`: Envia documento

#### Propriedades

- `is_connected`: Status da conexão
- `phone_number`: Número do WhatsApp conectado
- `qr_code`: QR Code atual (se disponível)

### Eventos

- `on_message(message)`: Chamado quando uma mensagem é recebida
- `on_connection()`: Chamado quando a conexão é estabelecida
- `on_disconnection()`: Chamado quando a conexão é perdida
- `on_qr(qr_code)`: Chamado quando um novo QR Code é gerado
- `on_ready()`: Chamado quando o cliente está pronto

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⚠️ Disclaimer

Esta biblioteca é para fins educacionais e de desenvolvimento. Use com responsabilidade e respeite os Termos de Serviço do WhatsApp.

## 🆘 Suporte

- **Issues**: [GitHub Issues](https://github.com/llongaray/pywhatsweb/issues)
- **Discussions**: [GitHub Discussions](https://github.com/llongaray/pywhatsweb/discussions)

---

Feito com ❤️ pela equipe TI Léo
