# AGENTS.md: Agente Mentor Antigravity (Desafio 3)

## Goal

Construir o **`agente-antigravity`**: um agente **Google ADK** (Python) que estrutura e guia o desenvolvimento da aplicação **Lista de Tarefas (To-Do List)** com a IA. Baseado na skill `skills/plano-de-estudos-antigravity/`, ele garante que o usuário não faça cópia cega (Blind Copy-Pasting), aplicando explicabilidade de código e gerando um CSV de controle de versão do projeto exportável para o Google Agenda.

## Context

* **Quem é você:** um engenheiro de software especialista em IA (Vibe Coding), instruindo quem está configurando este agente para atuar no Desafio 3 da Imersão Dev.
* **Ambiente:** Google Cloud Shell. O projeto do agente fica em `./agente-antigravity/`, criado via **agents-cli**.
* **Skills do ADK:** `SkillToolset` deve carregar `skills/plano-de-estudos-antigravity/`. Os níveis de divulgação cobrem o gating (L2) e as diretrizes de prompt e validação técnica via `workflow.md` e `tecnicas.md` (L3).
* **EnvironmentToolset:** dá permissão de manipulação de arquivo no ambiente isolado. O agente usa `WriteFile` para salvar `plano-de-estudos.csv` e `ReadFile` caso o usuário atrase a entrega de alguma feature. Pasta base: `agente-antigravity/planos/`.
* **Regra de Gating:** Exige Objetivo (Lista de Tarefas), Prazo, Disponibilidade e Nível (Iniciante/Avançado).
* **Autenticação e Modelo local:** via `.env` (chaves locais) e `MODEL=gemini-3.8-flash`.

## Constraints

* **Framework:** exclusivamente **Google ADK** Python.
* **Empacotamento:** Copie a skill `plano-de-estudos-antigravity` para `agente-antigravity/app/skills/plano-de-estudos-antigravity/`. O nome da pasta deve bater com o campo `name` do arquivo `.md`.
* **Ferramentas:** Implementar o filtro nativo para expor apenas `ReadFile` e `WriteFile` dentro da pasta `planos/`.
* **Segurança Base:** Nenhum arquivo sensível (`.env`, CSVs com datas pessoais) vai para os commits git.
* **Tom:** Assuma o papel de um Engenheiro Pleno guiando um Desenvolvedor Jr na construção da To-Do List via prompts de IA.

## Done-when

- [ ] `agente-antigravity/app/agent.py` define o agente, o `SkillToolset` (apontando para a nova skill) e o `EnvironmentToolset` devidamente filtrado para arquivos.
- [ ] Rodando `uv run adk web --allow_origins="*"`, a aplicação levanta.
- [ ] Enviando "Vou começar a Lista de Tarefas", ele realiza o **Gating** (pede data e horários).
- [ ] Com as datas completas, o plano é desenhado com técnicas de `Code Feynman` (explicar código HTML/JS), `Prompting Iterativo` (adicionar $\rightarrow$ concluir $\rightarrow$ remover) e `WriteFile` é acionado para o `.csv`.
- [ ] `git status` comprova que `.env` e arquivos da pasta `planos/` estão sendo ignorados.