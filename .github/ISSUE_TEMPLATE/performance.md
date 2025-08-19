---
name: Performance
about: Report performance issues or suggest optimizations
title: '[PERF] '
labels: 'performance'
assignees: ''

---

## ⚡ Tipo de Problema de Performance
- [ ] 🐌 Operação muito lenta
- [ ] 💾 Uso excessivo de memória
- [ ] 🔄 Timeout em operações
- [ ] 📱 Consumo excessivo de CPU
- [ ] 🌐 Largura de banda excessiva
- [ ] 💽 Uso excessivo de disco
- [ ] 🔌 Conexões não fechadas
- [ ] Outro: _________

## 📋 Descrição
Descreva o problema de performance que você está enfrentando.

## 🔍 Operação Afetada
**Qual funcionalidade está lenta?**
- [ ] Conexão inicial
- [ ] Geração de QR Code
- [ ] Envio de mensagens
- [ ] Recebimento de mensagens
- [ ] Criação de grupos
- [ ] Upload de mídia
- [ ] Outro: _________

## 📊 Métricas de Performance
**Tempo de execução:**
- Operação atual: [ex: 30 segundos]
- Tempo esperado: [ex: 5 segundos]
- Degradação: [ex: 6x mais lento]

**Uso de recursos:**
- CPU: [ex: 80% constante]
- Memória: [ex: 500MB]
- Disco: [ex: 100MB/s]

## 💻 Código de Exemplo
Inclua o código que está causando problemas de performance:

```python
from pywhatsweb import WhatsAppClient

# Código problemático aqui
client = WhatsAppClient()
# ...
```

## 🔍 Ambiente de Teste
**Configuração do sistema:**
- **OS**: [ex: Windows 10, macOS 10.15, Ubuntu 20.04]
- **Python**: [ex: 3.8, 3.9, 3.10]
- **PyWhatsWeb**: [ex: 0.1.0]
- **Chrome**: [ex: 90.0.4430.212]
- **RAM**: [ex: 8GB, 16GB]
- **CPU**: [ex: Intel i5, AMD Ryzen 5]
- **Disco**: [ex: SSD, HDD]

**Configurações específicas:**
- Modo headless: [ex: True/False]
- Timeout: [ex: 30 segundos]
- Debug: [ex: True/False]

## 📈 Cenário de Uso
**Como você está usando a biblioteca?**
- [ ] Uso único (uma operação por vez)
- [ ] Uso em lote (múltiplas operações)
- [ ] Uso contínuo (24/7)
- [ ] Uso em produção
- [ ] Uso em desenvolvimento
- [ ] Outro: _________

**Volume de dados:**
- Número de mensagens: [ex: 1000 por hora]
- Tamanho de arquivos: [ex: 10MB]
- Número de contatos: [ex: 500]

## 🎯 Impacto
**Quem é afetado:**
- [ ] Usuário individual
- [ ] Equipe de desenvolvimento
- [ ] Usuários em produção
- [ ] Outro: _________

**Severidade:**
- [ ] Baixa (inconveniente)
- [ ] Média (afeta usabilidade)
- [ ] Alta (afeta funcionalidade)
- [ ] Crítica (impede uso)

## 🔧 Soluções Tentadas
Liste o que você já tentou para resolver o problema:
- [ ] Ajustei timeouts
- [ ] Mudei configurações do Chrome
- [ ] Reduzi volume de dados
- [ ] Reiniciei o sistema
- [ ] Outro: _________

## 💡 Sugestões de Otimização
Se você tem ideias para melhorar a performance, descreva-as aqui.

## 📸 Screenshots (se aplicável)
Adicione screenshots de monitores de performance, logs ou gráficos.

## 📊 Logs de Performance
Se aplicável, inclua logs relevantes:

```
[INFO] Operação iniciada: 2024-01-01 10:00:00
[INFO] Operação concluída: 2024-01-01 10:00:30
[WARNING] Timeout atingido: 30 segundos
```

## 📞 Informações Adicionais
Adicione qualquer outro contexto sobre o problema de performance aqui.

---

**💡 Dica**: Para problemas de performance, é útil incluir métricas quantitativas e logs detalhados para ajudar na investigação.
