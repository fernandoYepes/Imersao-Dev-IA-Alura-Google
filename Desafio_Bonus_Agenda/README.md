# 🧠 Imersão Dev Engenharia de Software na Era da IA: Agente de Antigravity (Desafio 3)

Neste lab você vai usar o **Antigravity CLI (`agy`)** para criar, com o **Google ADK**, um agente especialista em pair programming com IA. O agente usa a skill [`plano-de-estudos-antigravity`](skills/plano-de-estudos-antigravity/SKILL.md): você fornece o objetivo (criar uma Lista de Tarefas) e ele estrutura as sessões de prompt iterativo, testes manuais/automáticos e salva o roteiro em CSV no Google Agenda usando o [EnvironmentToolset](https://adk.dev/integrations/environment-toolset/) do ADK.

## Pré-requisitos

- Conta Google com um projeto do Google Cloud com faturamento ativo (os créditos do [free trial](https://cloud.google.com/free) servem)
- Chave de API do Google AI Studio, criada em [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- Conta no GitHub

---

# Aula 3: Introdução ao Antigravity CLI

## 1. Preparar o Cloud Shell

Abra o [Console do Google Cloud](https://console.cloud.google.com/), selecione o seu projeto e clique em **Ativar o Cloud Shell** (ícone `>_`). Depois rode:

```bash
export PROJECT_ID=$(gcloud config get-value project)
echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> ~/.bashrc

# Habilita a Agent Platform (acesso aos modelos usados pelo agy)
gcloud services enable aiplatform.googleapis.com cloudaicompanion.googleapis.com

git clone https://github.com/johngarrido/alura-imersao-dev-agy.git ~/alura-imersao-dev
cd ~/alura-imersao-dev
```

> Se o Cloud Shell não abrir no projeto certo, rode `gcloud config set project SEU_PROJECT_ID` antes.

## 2. Instalar e configurar o `agy`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
curl -fsSL https://antigravity.google/cli/install.sh | bash
source ~/.bashrc
```

Para iniciar o Antigravity CLI, utilize o comando:

```bash
agy
```

No setup do `agy`, escolha:

1. `Use a Google Cloud project` → `Continue with Google Cloud`
2. Abra o link, autorize com a sua conta e cole o código no terminal
3. Cole o ID do projeto (`echo $PROJECT_ID`)
4. Location: `global` · License: `Agent Platform`
5. Aceite os termos e confirme `Yes, I trust this folder`

## 3. Primeiros passos no `agy`

Teste alguns comandos e prompts:

```text
/help
```

```text
Leia skills/plano-de-estudos-antigravity/SKILL.md e me explique como ela apoia o desenvolvimento guiado por IA.
```

Saia com `/exit`.

## 4. Instalar o agents-cli

```bash
uvx google-agents-cli setup
agy
```

No `agy`:

1. Rode `/skills` e confira se aparecem as skills `google-agents-cli-*`.
2. Rode `/config` e mude **Tool Permission** para `always-proceed`.

## 5. Criar o agente de Pair Programming

```text
/grill-me
```

O `agy` vai te entrevistar sobre o agente. Use estas respostas como base:

- **Objetivo:** um mentor que guia o usuário no Desafio 3 (Lista de Tarefas), dividindo o desenvolvimento em etapas de prompting, lógica JS, estilo e testes.
- **Skills:** usar a skill `skills/plano-de-estudos-antigravity`.
- **Comportamento:** se faltar a data limite de entrega ou o nível da pessoa, o agente pergunta.
- **Arquivos:** o agente salva a agenda do projeto em `plano-de-estudos.csv` usando o [EnvironmentToolset](https://adk.dev/integrations/environment-toolset/), focando nas permissões `ReadFile` e `WriteFile`.

Peça a criação do projeto:

```text
Crie um agente ADK chamado agente-antigravity seguindo as convenções do agents-cli e a especificação de ADK Skills. Copie a skill skills/plano-de-estudos-antigravity para agente-antigravity/app/skills/ e carregue-a com SkillToolset. Adicione o EnvironmentToolset com um LocalEnvironment na pasta agente-antigravity/planos/, expondo só as ferramentas ReadFile e WriteFile. O modelo vem da variável MODEL. Sem configuração de deploy.
```

Saia com `/exit`.

---

# Aula 4: Engenharia de software com IA e CLI

## 6. Configurar a API Key

```bash
cd ~/alura-imersao-dev/agente-antigravity
read -s -p "Cole sua API Key: " KEY && echo

cat << EOF > .env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GEMINI_API_KEY=${KEY}
MODEL=gemini-3.8-flash
EOF

uv sync
```

## 7. Testar no ADK Web (Roteiro do Desafio 3)

```bash
uv run adk web --allow_origins="*"
```

Clique no link no terminal. No ADK Web:

1. **Gating Check:** 
    ```text
    Quero fazer o Desafio 3 de criar a lista de tarefas.
    ```
    *(O agente deve perguntar o prazo, sua disponibilidade e seu nível de conhecimento)*.

2. **Geração Completa:**
    ```text
    Quero desenvolver a Lista de Tarefas (Desafio 3) com o Google Antigravity. Meu nível é iniciante. Tenho do dia 02/11 até o dia 06/11, estudando 1h por dia, das 19h às 20h.
    ```
    *(O agente irá usar as técnicas de Code Feynman e Prompt Iterativo, montando a agenda e salvando o CSV).*

No ADK Web, valide se a ferramenta `WriteFile` foi chamada com sucesso.

## 8. Evoluir o agente (Vibe Coding)

Abra uma segunda aba no Cloud Shell e rode:

```bash
cd ~/alura-imersao-dev
agy
```

**Validar o CSV gerado:**

```text
Leia agente-antigravity/planos/plano-de-estudos.csv e confira se ele contempla as funcionalidades de Adicionar, Marcar Concluída e Remover, conforme o Desafio 3.
```

## 9. Versionar no GitHub

Após finalizar, confira a ausência de `.env` e envie ao repositório conforme práticas Git padrão ensinadas.