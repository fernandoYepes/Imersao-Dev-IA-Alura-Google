# Salvar a Agenda do Projeto em CSV (`EnvironmentToolset`)

O agente utiliza as ferramentas do `EnvironmentToolset` para gerar e atualizar o arquivo da agenda de estudos do desafio de desenvolvimento com Google Antigravity.

---

## Ferramentas Autorizadas

| Ferramenta | Utilização no Contexto Antigravity | Argumentos |
|---|---|---|
| `WriteFile` | Grava ou substitui o plano de desenvolvimento em formato CSV | `path` (texto), `content` (texto) |
| `ReadFile` | Lê o cronograma salvo para verificar ou refatorar etapas atrasadas | `path` (texto), `start_line` e `end_line` |

*Atenção: Sempre salvar o arquivo inteiro de uma só vez usando `WriteFile`.*

## Regras de Formatação do Arquivo

* **Nome do arquivo:** usar impreterivelmente o caminho relativo `plano-de-estudos.csv`.
* **Proibido:** usar caminhos absolutos como `/tmp/...` ou subdiretórios inexistentes.
* **Formato das Datas e Horas:**
  - Datas no padrão dos EUA (`MM/DD/YYYY`).
  - Horários com especificação AM/PM (`HH:MM AM/PM`).

## Checklist do CSV de Estudos com Antigravity

Antes de invocar o `WriteFile`, confirme se o conteúdo do CSV segue os requisitos abaixo:

- [ ] Cabeçalho exato: `Subject,Start Date,Start Time,End Date,End Time,Description`
- [ ] Coluna `Subject`: Título direto da sessão (ex.: `📚 Antigravity: Prompt Inicial e Estrutura`).
- [ ] Coluna `Description`: Contém a técnica aplicada e o entregável visível no app, sempre delimitada por aspas duplas `""`.
- [ ] Sem blocos de código Markdown (```csv) dentro da string enviada para o arquivo.

### Exemplo de Estrutura Esperada

```csv
Subject,Start Date,Start Time,End Date,End Time,Description
📚 Antigravity: Estrutura Inicial,11/02/2026,07:00 PM,11/02/2026,08:00 PM,"Revisão: — | Técnica: Prompting Iterativo | Entregável: Interface básica com input gerada pelo Antigravity"
📚 Antigravity: Adicionar e Remover,11/03/2026,07:00 PM,11/03/2026,08:00 PM,"Revisão: Estrutura HTML/CSS (D+1) | Técnica: Code Feynman | Entregável: Funções de inclusão e exclusão ativas no JS"
```

## Retorno e Confirmação

* **Quando `WriteFile` retornar `status: ok`**: informe na seção 5 do documento gerado o caminho do arquivo e a quantidade de sessões cadastradas.
* **Em caso de erro na ferramenta**: exiba o bloco de código `.csv` diretamente no relatório da conversa para cópia manual pelo usuário.