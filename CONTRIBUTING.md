# Guia de Contribuição

Obrigado por considerar contribuir para o PyWhatsWeb! 🚀

## Como Contribuir

### Reportando Bugs

- Use o template de bug report
- Inclua informações detalhadas sobre seu ambiente
- Forneça passos para reproduzir o problema
- Adicione logs de erro quando possível

### Sugerindo Funcionalidades

- Use o template de feature request
- Descreva o problema que a funcionalidade resolveria
- Forneça exemplos de uso
- Considere a prioridade e categoria

### Enviando Pull Requests

1. **Fork o repositório**
2. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. **Faça suas mudanças**
4. **Adicione testes** para novas funcionalidades
5. **Execute os testes** localmente
6. **Commit suas mudanças**
   ```bash
   git commit -m "feat: adiciona nova funcionalidade"
   ```
7. **Push para sua branch**
   ```bash
   git push origin feature/nova-funcionalidade
   ```
8. **Abra um Pull Request**

## Padrões de Código

### Python

- Siga o PEP 8
- Use type hints
- Documente funções e classes
- Mantenha linhas com no máximo 88 caracteres (Black)

### Formatação

- Use Black para formatação automática
- Use isort para ordenação de imports
- Execute `make format` antes de commitar

### Testes

- Mantenha cobertura de testes acima de 80%
- Adicione testes para novas funcionalidades
- Use mocks para dependências externas
- Execute `make test` antes de commitar

## Ambiente de Desenvolvimento

### Instalação

```bash
# Clone o repositório
git clone https://github.com/llongaray/pywhatsweb.git
cd pywhatsweb

# Instale em modo desenvolvimento
pip install -e ".[dev]"

# Configure pre-commit
pre-commit install
```

### Comandos Úteis

```bash
# Executar testes
make test

# Verificar qualidade de código
make lint

# Formatar código
make format

# Limpar arquivos temporários
make clean

# Construir pacote
make build

# Verificar build
make build-check
```

## Estrutura do Projeto

```
pywhatsweb/
├── pywhatsweb/          # Código fonte principal
│   ├── __init__.py
│   ├── client.py        # Cliente principal
│   ├── config.py        # Configurações
│   ├── models.py        # Modelos de dados
│   ├── exceptions.py    # Exceções personalizadas
│   └── cli.py          # Interface de linha de comando
├── tests/               # Testes
├── examples/            # Exemplos de uso
├── docs/                # Documentação
└── requirements*.txt    # Dependências
```

## Processo de Release

1. **Atualize a versão** em `pyproject.toml` e `setup.py`
2. **Atualize o CHANGELOG.md**
3. **Crie uma tag** para a versão
4. **Execute os testes** completos
5. **Construa o pacote** com `make build`
6. **Verifique o build** com `make build-check`
7. **Publique no PyPI** com `make publish`

## Comunicação

- **Issues**: Use o GitHub Issues para bugs e funcionalidades
- **Discussões**: Use o GitHub Discussions para perguntas gerais
- **Email**: ti.leo@example.com para assuntos privados

## Agradecimentos

Obrigado por contribuir para tornar o PyWhatsWeb melhor! 🎉

---

**Lembre-se**: Este é um projeto da comunidade. Seja respeitoso, construtivo e ajude outros contribuidores a crescer.
