---
name: Compatibility
about: Report compatibility issues with different systems or versions
title: '[COMPAT] '
labels: 'compatibility'
assignees: ''

---

## 🔄 Tipo de Problema de Compatibilidade
- [ ] 🐍 Incompatibilidade com versão do Python
- [ ] 💻 Problema específico do sistema operacional
- [ ] 🌐 Problema com versão do Chrome
- [ ] 🔌 Problema com ChromeDriver
- [ ] 📱 Problema com arquitetura (x64, ARM64)
- [ ] 🐳 Problema com Docker
- [ ] 🔧 Problema com dependências
- [ ] Outro: _________

## 📋 Descrição
Descreva o problema de compatibilidade que você está enfrentando.

## 🚨 Erro Completo
Cole aqui a mensagem de erro completa:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    from pywhatsweb import WhatsAppClient
ImportError: [erro específico]
```

## 🔍 Ambiente Afetado
**Sistema operacional:**
- [ ] Windows 10/11
- [ ] Windows 8.1
- [ ] Windows 7
- [ ] macOS 10.15+
- [ ] macOS 10.14
- [ ] Ubuntu 18.04+
- [ ] Ubuntu 16.04
- [ ] CentOS 7
- [ ] CentOS 8
- [ ] Outro: _________

**Arquitetura:**
- [ ] x64 (AMD64)
- [ ] x86 (32-bit)
- [ ] ARM64 (Apple Silicon)
- [ ] ARM32
- [ ] Outro: _________

**Versão do Python:**
- [ ] Python 3.7
- [ ] Python 3.8
- [ ] Python 3.9
- [ ] Python 3.10
- [ ] Python 3.11
- [ ] Python 3.12
- [ ] Outro: _________

## 🌐 Navegador e Driver
**Versão do Chrome:**
- [ ] Chrome 90+
- [ ] Chrome 80-89
- [ ] Chrome 70-79
- [ ] Chrome 60-69
- [ ] Chrome < 60
- [ ] Chromium
- [ ] Outro: _________

**Versão do ChromeDriver:**
- [ ] ChromeDriver 90+
- [ ] ChromeDriver 80-89
- [ ] ChromeDriver 70-79
- [ ] ChromeDriver 60-69
- [ ] ChromeDriver < 60
- [ ] Gerenciado automaticamente
- [ ] Outro: _________

## 🔧 Dependências
**Versões das dependências principais:**
```bash
# Cole aqui o resultado de:
pip list | grep -E "(selenium|webdriver-manager|requests|python-dotenv|qrcode|pillow)"
```

## 💻 Ambiente de Desenvolvimento
**Ferramentas e configurações:**
- **IDE/Editor**: [ex: VS Code, PyCharm, Vim]
- **Ambiente virtual**: [ex: venv, virtualenv, conda]
- **Gerenciador de pacotes**: [ex: pip, poetry, pipenv]
- **Versão do pip**: [ex: 21.0.0]

## 🔍 Cenário de Uso
**Como você está usando a biblioteca:**
- [ ] Desenvolvimento local
- [ ] Testes automatizados
- [ ] Produção
- [ ] CI/CD
- [ ] Container Docker
- [ ] Outro: _________

## 📊 Comportamento Esperado vs. Atual
**O que deveria acontecer:**
Descreva o comportamento esperado.

**O que está acontecendo:**
Descreva o comportamento atual.

## 🧪 Teste de Compatibilidade
**Execute este código de teste e cole o resultado:**

```python
import sys
import platform
import subprocess

print(f"Python: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Architecture: {platform.architecture()}")
print(f"Machine: {platform.machine()}")

try:
    import selenium
    print(f"Selenium: {selenium.__version__}")
except ImportError:
    print("Selenium: Não instalado")

try:
    import webdriver_manager
    print(f"WebDriver Manager: {webdriver_manager.__version__}")
except ImportError:
    print("WebDriver Manager: Não instalado")
```

## 🔍 Passos para Reproduzir
Descreva os passos para reproduzir o problema:

1. [Passo 1]
2. [Passo 2]
3. [Passo 3]
4. [Resultado]

## 💡 Soluções Tentadas
Liste o que você já tentou para resolver o problema:

- [ ] Atualizei o Python
- [ ] Atualizei o Chrome
- [ ] Atualizei o ChromeDriver
- [ ] Reinstalei as dependências
- [ ] Usei um ambiente virtual diferente
- [ ] Outro: _________

## 📸 Screenshots (se aplicável)
Adicione screenshots que demonstrem o problema de compatibilidade.

## 🔗 Links Úteis
**Recursos consultados:**
- [ ] Documentação oficial
- [ ] Issues do GitHub
- [ ] Stack Overflow
- [ ] Outro: _________

## 📞 Informações Adicionais
Adicione qualquer outro contexto sobre o problema de compatibilidade aqui.

## 🎯 Impacto
**Quem é afetado:**
- [ ] Usuário individual
- [ ] Equipe de desenvolvimento
- [ ] Usuários em produção
- [ ] Outro: _________

**Severidade:**
- [ ] Baixa (inconveniente)
- [ ] Média (afeta desenvolvimento)
- [ ] Alta (afeta funcionalidade)
- [ ] Crítica (impede uso)

---

**💡 Dicas de Compatibilidade**:
- Use sempre a versão mais recente do Python suportada
- Mantenha o Chrome atualizado
- Use ambientes virtuais para isolar dependências
- Teste em diferentes sistemas antes de fazer deploy

**🔗 Recursos Úteis**:
- [Requisitos do Sistema](README.md#requisitos)
- [Guia de Instalação](README.md#instalação)
- [Problemas Comuns](SUPPORT.md#problemas-comuns)
