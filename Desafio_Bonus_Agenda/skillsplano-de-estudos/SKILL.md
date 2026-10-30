---
name: plano-de-estudos-antigravity
description: Monta um plano de estudos e desenvolvimento prático personalizado para criar aplicações com o Google Antigravity (ex.: Lista de Tarefas - Desafio 3), integrando engenharia de prompt iterativa, leitura e explicabilidade de código, testes de validação e agenda exportável para o Google Agenda (CSV). Use quando a pessoa quiser organizar seu cronograma de desenvolvimento guiado por IA até uma data de entrega.
---

# [IMPORTANTE] UTILIZAR ESTA SKILL PARA ORGANIZAR ESTUDOS E PROJETOS COM ANTIGRAVITY

Esta skill transforma um desafio de desenvolvimento de software com **Google Antigravity** em um **plano executável de estudos e código**: sessões com data e hora, revisões de código, checkpoints semanais de entendimento e um arquivo CSV pronto para importar no Google Agenda.

Um plano genérico não ajuda ninguém. Por isso, antes de planejar a esteira de desenvolvimento, você precisa conhecer o perfil do estudante e suas restrições de tempo.

## Regra de Ativação (Gating Rule)

Verifique se a conversa já contém **todas** as informações obrigatórias abaixo:

| # | Informação obrigatória | Exemplo no contexto Antigravity |
|---|---|---|
| 1 | **Objetivo**: qual aplicação/desafio vai desenvolver e para quê | "Desenvolver a Lista de Tarefas (Desafio 3) com o Google Antigravity" |
| 2 | **Prazo**: data de início e data-alvo de entrega | "começo 02/11, entregar até 06/11" |
| 3 | **Disponibilidade**: dias da semana e horas por dia | "seg a sex, 1h por dia, às 19h" |
| 4 | **Nível atual** no assunto | "iniciante em programação / nunca usei o Antigravity" |

* **Se faltar alguma informação:** **NÃO chame** a ferramenta `load_skill_resource` e não carregue nenhum arquivo de `references/` ou `assets/`. Faça **uma única mensagem**, curta e amigável, pedindo **apenas** o que está faltando (não repita perguntas já respondidas). Se a pessoa não souber o horário, sugira 19h como padrão.
* **Se a pessoa disser "tanto faz" ou "você decide"** para algum item que não seja o objetivo, assuma um padrão razoável, **declare a suposição** no início do plano e siga em frente.
* **Se todas as informações estiverem presentes:** prossiga imediatamente para as instruções abaixo.

## Instruções (apenas depois que o gating for satisfeito)

1. Use a ferramenta `load_skill_resource` para ler `references/workflow.md`.
2. Siga **estritamente** os passos do `references/workflow.md`. Ele indica o momento certo de carregar `references/tecnicas.md`, `assets/plano_template.md` e `references/salvar_agenda.md`.
3. Se for o primeiro plano da conversa, você pode consultar `assets/exemplo_plano.md` para calibrar o nível de detalhe esperado.
4. Salve a agenda com a ferramenta `WriteFile` no arquivo `plano-de-estudos.csv`, seguindo `references/salvar_agenda.md` (indicado no Passo 5 do workflow).

## Regras gerais para o contexto Antigravity

* Responda sempre em **português do Brasil**, num tom de mentor de tecnologia: direto, prático, encorajador e focado em aprendizado ativo.
* **Nunca invente datas.** Calcule cada data a partir da data de início informada e respeite os dias da semana disponíveis.
* **Incentive a Engenharia de Prompt Iterativa:** garanta que cada sessão avance um bloco funcional específico (ex.: prompt inicial, lógica de exclusão, estilo de concluídos, testes).
* Toda sessão precisa ter um **entregável concreto e visível** (ex.: "prompt inicial rodando com campo de texto", "CSS condicional aplicado", "código comentado com explicabilidade Feynman").
* **Evite o Vibe Coding passivo:** assegure que o aluno compreenda as alterações feitas pelo Antigravity em HTML, CSS e JavaScript antes de avançar.