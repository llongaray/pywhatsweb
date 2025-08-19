# Suporte

## Como Obter Ajuda

### 📚 Documentação
- **README.md**: Visão geral e exemplos básicos
- **Exemplos**: Pasta `examples/` com casos de uso práticos
- **API Reference**: Documentação completa das classes e métodos

### 🐛 Reportando Problemas
Se você encontrou um bug ou tem uma sugestão:

1. **Verifique se já foi reportado**: Procure nos [Issues](https://github.com/llongaray/pywhatsweb/issues) existentes
2. **Use o template correto**: 
   - [Bug Report](https://github.com/llongaray/pywhatsweb/issues/new?template=bug_report.md) para problemas
   - [Feature Request](https://github.com/llongaray/pywhatsweb/issues/new?template=feature_request.md) para sugestões
3. **Inclua informações detalhadas**: Sistema operacional, versão do Python, logs de erro, etc.

### 💬 Discussões
- **GitHub Discussions**: Para perguntas gerais, dúvidas e conversas
- **Issues**: Para bugs confirmados e funcionalidades

### 📧 Contato Direto
- **Email**: ti.leo@example.com
- **Assunto**: Inclua "PyWhatsWeb" no assunto

## Problemas Comuns

### ❌ Erro de Conexão
```
pywhatsweb.exceptions.ConnectionError: Falha ao conectar
```

**Soluções:**
- Verifique se o Google Chrome está instalado
- Certifique-se de que tem conexão com a internet
- Tente executar sem modo headless primeiro

### ❌ QR Code não aparece
```
pywhatsweb.exceptions.AuthenticationError: QR Code não foi gerado
```

**Soluções:**
- Aguarde mais tempo para o WhatsApp Web carregar
- Verifique se não há bloqueios de firewall
- Tente em modo não-headless

### ❌ Mensagem não enviada
```
pywhatsapp.exceptions.MessageError: Falha ao enviar mensagem
```

**Soluções:**
- Verifique se o número está no formato correto (com código do país)
- Certifique-se de que está conectado ao WhatsApp
- Aguarde a conexão estabilizar antes de enviar

### ❌ ChromeDriver não encontrado
```
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary
```

**Soluções:**
- Instale o Google Chrome
- A biblioteca gerencia o ChromeDriver automaticamente
- Em alguns sistemas, pode ser necessário instalar manualmente

## Ambiente de Desenvolvimento

### 🔧 Configuração Local
```bash
# Clone o repositório
git clone https://github.com/llongaray/pywhatsweb.git
cd pywhatsweb

# Instale em modo desenvolvimento
pip install -e ".[dev]"

# Configure pre-commit
pre-commit install

# Execute testes
make test
```



### 🧪 Executando Testes
```bash
# Todos os testes
make test

# Testes específicos
pytest tests/test_client.py -v

# Com cobertura
pytest --cov=pywhatsweb --cov-report=html
```

## Contribuindo

### 📝 Padrões de Código
- Use Black para formatação
- Siga PEP 8
- Adicione type hints
- Documente funções e classes

### 🚀 Processo de Contribuição
1. Fork o repositório
2. Crie uma branch para sua feature
3. Faça suas mudanças
4. Adicione testes
5. Execute `make check-all`
6. Abra um Pull Request

## Recursos Adicionais

### 🔗 Links Úteis
- [WhatsApp Web](https://web.whatsapp.com/)
- [Selenium Python](https://selenium-python.readthedocs.io/)
- [Python Documentation](https://docs.python.org/)

### 📖 Tutoriais
- [Primeiros Passos](examples/basic_usage.py)
- [Uso com Eventos](examples/basic_usage.py#example_with_events)
- [Configuração Avançada](README.md#configuração)

### 🆘 Ainda Precisa de Ajuda?
Se nenhuma das opções acima resolveu seu problema:

1. **Crie um issue detalhado** com todas as informações
2. **Inclua logs completos** e screenshots se aplicável
3. **Descreva o ambiente** exato onde está testando
4. **Mencione o que já tentou** para resolver

---

**Lembre-se**: Estamos aqui para ajudar! Quanto mais detalhes você fornecer, mais rápido poderemos resolver seu problema. 🚀
