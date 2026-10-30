# Técnicas de Aprendizado de Software com Google Antigravity

Este guia orienta a aplicação de técnicas baseadas em evidência no contexto de **Desenvolvimento de Software Guiado por IA (Vibe Coding consciente)**. Evite o aprendizado passivo (apenas copiar e colar código sem leitura).

---

## Técnicas de alta eficácia para Devs

### 1. Engenharia de Prompt Iterativa (*Step-by-Step Prompting*)
* **O que é:** Construir a aplicação em pequenos blocos de instruções claras para o Google Antigravity, em vez de pedir o sistema inteiro de uma só vez.
* **Quando usar:** Na criação de novas telas, adição de comportamentos e refatoração visual.
* **Entregável típico:** Registro das mensagens/prompts enviados e o resultado obtido na interface.

### 2. Explicabilidade de Código de Memória (*Code Feynman*)
* **O que é:** Pedir para o Google Antigravity gerar a funcionalidade e, em seguida, explicar em voz alta ou em poucas frases o papel de cada bloco de código (HTML, CSS, JS).
* **Quando usar:** Sempre que a IA implementar uma nova função lógica (ex.: `array.filter`, `addEventListener`).
* **Entregável típico:** Um parágrafo com as próprias palavras anotado como comentário no próprio código.

### 3. Validação por Testes Automáticos e Manuais (*Test-Driven Check*)
* **O que é:** Solicitar que o Google Antigravity crie e execute testes na aplicação para verificar se o novo código não quebrou funcionalidades anteriores (regressão).
* **Quando usar:** Após implementar alterações de estilo visual ou remoção de elementos.
* **Entregável típico:** Checklist de validação com 100% dos testes aprovados no console/ambiente.

### 4. Recuperação Ativa de Sintaxe (*Active Recall Dev*)
* **O que é:** Tentar escrever um trecho simples (ex.: um seletor CSS ou botão HTML) antes de pedir para a IA, conferindo a sintaxe depois.
* **Quando usar:** No aquecimento das sessões de estudo.
* **Entregável típico:** Função simples ou regra de estilo escrita manualmente sem ajuda da IA.

### 5. Depuração Assistida (*AI-Assisted Debugging*)
* **O que é:** Diante de um erro, colar a mensagem no Antigravity e pedir para ele identificar a causa raiz **e** explicar a correção necessária.
* **Quando usar:** Quando a interface não responder como o esperado ao clicar ou digitar.
* **Entregável típico:** Registro do bug encontrado e da solução aplicada.

---

## Gestão de Tempo e Blocos de Trabalho

### Estrutura da Sessão no Antigravity (1 Hora)
1. **Aquecimento / Leitura do Código Anterior** (10 min): Abrir o projeto e explicar o que o código atual faz.
2. **Iteração com o Antigravity** (35 min): Enviar o prompt do dia, aplicar a mudança e testar na interface.
3. **Documentação e Checkpoint** (15 min): Pedir explicação da mudança, comentar o código e preencher a entrega do dia.

---

## Antipadrões em Projetos com IA (O que EVITAR)

| Antipadrão | Por que evitar | Substituir por |
|---|---|---|
| **Blind Copy-Pasting** | O estudante não aprende o funcionamento e fica incapaz de corrigir erros simples. | Explicabilidade de Código (Code Feynman) antes de aceitar a mudança. |
| **Prompt Monolítico** | Enviar 10 requisitos de uma vez faz a IA gerar código muito complexo de uma só vez. | Engenharia de Prompt Iterativa (1 requisito por vez). |
| **Negligenciar o Console/Testes** | Achar que a interface funciona só porque "parece bonita", sem testar cenários de borda. | Test-Driven Check com o Antigravity. |
| **Pular a Leitura dos Diff de Código** | Aceitar substituições no arquivo sem ver quais arquivos foram alterados. | Pedir ao Antigravity para listar quais partes do arquivo mudaram. |