---
name: Security
about: Report security vulnerabilities or concerns
title: '[SECURITY] '
labels: 'security'
assignees: ''

---

## 🔒 Tipo de Problema de Segurança
- [ ] 🚨 Vulnerabilidade crítica
- [ ] ⚠️ Vulnerabilidade de média severidade
- [ ] 💡 Problema de segurança menor
- [ ] 🔍 Comportamento suspeito
- [ ] 📱 Exposição de dados sensíveis
- [ ] 🔐 Problema de autenticação
- [ ] 🌐 Problema de rede
- [ ] Outro: _________

## 📋 Descrição
Descreva o problema de segurança de forma clara e concisa.

**⚠️ IMPORTANTE**: Para vulnerabilidades críticas, considere usar nosso [processo de divulgação responsável](SECURITY.md) em vez de abrir um issue público.

## 🔍 Categoria da Vulnerabilidade
**Tipo de vulnerabilidade:**
- [ ] Injeção de código
- [ ] Exposição de dados sensíveis
- [ ] Quebra de autenticação
- [ ] Elevação de privilégios
- [ ] Cross-site scripting (XSS)
- [ ] Cross-site request forgery (CSRF)
- [ ] Injeção SQL
- [ ] Deserialização insegura
- [ ] Outro: _________

## 📊 Severidade
**Classificação da vulnerabilidade:**
- [ ] **Crítica** - Pode resultar em comprometimento completo do sistema
- [ ] **Alta** - Pode resultar em acesso não autorizado ou perda de dados
- [ ] **Média** - Pode resultar em vazamento de informações ou degradação de serviço
- [ ] **Baixa** - Impacto limitado ou baixo risco

## 🎯 Impacto
**O que pode ser afetado:**
- [ ] Dados do usuário
- [ ] Credenciais de acesso
- [ ] Funcionalidades da biblioteca
- [ ] Sistema operacional
- [ ] Outros aplicativos
- [ ] Outro: _________

**Quem pode ser afetado:**
- [ ] Usuários individuais
- [ ] Sistemas em produção
- [ ] Desenvolvedores
- [ ] Outro: _________

## 💻 Código de Exemplo
Se aplicável, inclua o código que demonstra a vulnerabilidade:

```python
# Código vulnerável (se aplicável)
from pywhatsweb import WhatsAppClient

# Exemplo do problema
client = WhatsAppClient()
# ...
```

## 🔍 Passos para Reproduzir
Descreva os passos para reproduzir o problema de segurança:

1. [Passo 1]
2. [Passo 2]
3. [Passo 3]
4. [Resultado esperado vs. atual]

## 📊 Ambiente de Teste
**Configuração do sistema:**
- **OS**: [ex: Windows 10, macOS 10.15, Ubuntu 20.04]
- **Python**: [ex: 3.8, 3.9, 3.10]
- **PyWhatsWeb**: [ex: 0.1.0]
- **Chrome**: [ex: 90.0.4430.212]
- **Configurações de segurança**: [ex: Firewall, antivírus, etc.]

## 🛡️ Mitigações Atuais
**O que já está sendo feito para proteger:**
- [ ] Validação de entrada
- [ ] Sanitização de dados
- [ ] Controle de acesso
- [ ] Criptografia
- [ ] Outro: _________

## 💡 Sugestões de Correção
Se você tem ideias para corrigir o problema, descreva-as aqui.

## 📸 Evidências (se aplicável)
Adicione screenshots, logs ou outras evidências que demonstrem o problema.

## 🔐 Informações Sensíveis
**⚠️ AVISO**: NÃO inclua:
- Senhas reais
- Tokens de acesso
- Dados pessoais
- Informações de produção

## 📞 Contato de Segurança
Para vulnerabilidades críticas, você pode nos contatar diretamente:
- **Email**: ti.leo@example.com
- **Assunto**: [SECURITY] PyWhatsWeb - [Descrição breve]

## 📋 Checklist de Segurança
- [ ] ✅ Não incluí informações sensíveis
- [ ] ✅ Descrevi o impacto claramente
- [ ] ✅ Forneci passos para reproduzir
- [ ] ✅ Incluí informações do ambiente
- [ ] ✅ Considerei o processo de divulgação responsável

## 📞 Informações Adicionais
Adicione qualquer outro contexto sobre o problema de segurança aqui.

---

**🔒 Política de Segurança**: Para vulnerabilidades críticas, consulte nossa [política de segurança](SECURITY.md) para o processo de divulgação responsável.

**💡 Dica**: Se você é um pesquisador de segurança, considere participar de nosso programa de bug bounty (se disponível).
