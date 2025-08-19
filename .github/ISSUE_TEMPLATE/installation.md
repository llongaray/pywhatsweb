---
name: Installation
about: Report installation issues or problems
title: '[INSTALL] '
labels: 'installation'
assignees: ''

---

## 📦 Tipo de Problema de Instalação
- [ ] 🚫 Falha na instalação via pip
- [ ] 🔧 Falha na instalação em modo desenvolvimento
- [ ] 🐳 Problema com Docker
- [ ] 📱 Dependências não encontradas
- [ ] 🔌 Problema com Chrome/ChromeDriver
- [ ] 🐍 Incompatibilidade de versão do Python
- [ ] 💻 Problema específico do sistema operacional
- [ ] Outro: _________

## 📋 Descrição
Descreva o problema de instalação que você está enfrentando.

## 🚨 Erro Completo
Cole aqui a mensagem de erro completa:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <package>
    import pywhatsweb
ModuleNotFoundError: No module named 'pywhatsweb'
```

## 💻 Comando Executado
**Qual comando você executou?**
```bash
# Exemplo:
pip install pywhatsweb
# ou
pip install -e .
# ou
docker build -t pywhatsweb .
```

## 🔍 Ambiente de Instalação
**Sistema operacional:**
- [ ] Windows 10/11
- [ ] macOS 10.15+
- [ ] Ubuntu 18.04+
- [ ] CentOS/RHEL
- [ ] Outro: _________

**Versão do Python:**
- [ ] Python 3.8
- [ ] Python 3.9
- [ ] Python 3.10
- [ ] Python 3.11
- [ ] Python 3.12
- [ ] Outro: _________

**Gerenciador de pacotes:**
- [ ] pip
- [ ] conda
- [ ] poetry
- [ ] pipenv
- [ ] Outro: _________

**Ambiente virtual:**
- [ ] venv
- [ ] virtualenv
- [ ] conda env
- [ ] Não estou usando
- [ ] Outro: _________

## 🔧 Configuração do Sistema
**Detalhes adicionais:**
- **Arquitetura**: [ex: x64, ARM64]
- **RAM**: [ex: 8GB, 16GB]
- **Espaço em disco**: [ex: 50GB livre]
- **Permissões**: [ex: Usuário normal, Administrador]
- **Firewall/Antivírus**: [ex: Windows Defender, Avast]

## 📱 Dependências do Sistema
**Chrome instalado:**
- [ ] ✅ Sim, versão [ex: 90.0.4430.212]
- [ ] ❌ Não
- [ ] ❓ Não sei

**ChromeDriver:**
- [ ] ✅ Sim, versão [ex: 90.0.4430.24]
- [ ] ❌ Não
- [ ] ❓ Não sei
- [ ] 🔄 A biblioteca deve gerenciar automaticamente

## 🐳 Docker (se aplicável)
**Versão do Docker:**
- [ ] Docker Desktop
- [ ] Docker Engine
- [ ] Docker Compose
- [ ] Outro: _________

**Versão:**
```bash
docker --version
# Resultado: [cole aqui]
```

## 🔍 Passos Tentados
Liste o que você já tentou para resolver o problema:

1. [ ] Reinstalei o Python
2. [ ] Atualizei o pip
3. [ ] Criei um novo ambiente virtual
4. [ ] Instalei o Chrome
5. [ ] Baixei o ChromeDriver manualmente
6. [ ] Reiniciei o sistema
7. [ ] Outro: _________

## 📊 Logs de Instalação
Se aplicável, inclua logs detalhados da instalação:

```bash
pip install pywhatsweb -v
# Resultado: [cole aqui]
```

## 🎯 Resultado Esperado
Descreva o que você esperava que acontecesse durante a instalação.

## 📸 Screenshots (se aplicável)
Adicione screenshots da tela de erro ou terminal.

## 🔍 Verificações Adicionais
**Execute estes comandos e cole os resultados:**

```bash
# Versão do Python
python --version

# Versão do pip
pip --version

# Variáveis de ambiente
echo $PATH  # Linux/macOS
echo %PATH% # Windows

# Verificar se o Python está no PATH
which python  # Linux/macOS
where python  # Windows
```

## 📞 Informações Adicionais
Adicione qualquer outro contexto sobre o problema de instalação aqui.

## 💡 Soluções Alternativas
Se você encontrou uma solução alternativa, descreva-a aqui.

---

**💡 Dicas de Instalação**:
- Certifique-se de que o Python está no PATH do sistema
- Use um ambiente virtual para evitar conflitos
- Verifique se tem permissões de administrador (se necessário)
- Para problemas com Chrome, tente instalar a versão mais recente

**🔗 Recursos Úteis**:
- [Guia de Instalação](README.md#instalação)
- [Problemas Comuns](SUPPORT.md#problemas-comuns)
- [Configuração do Ambiente](CONTRIBUTING.md#ambiente-de-desenvolvimento)
