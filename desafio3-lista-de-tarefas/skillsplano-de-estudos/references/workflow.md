# Fluxo de Trabalho: Montagem do Plano de Estudos (Google Antigravity)

Siga os passos na ordem. Não pule etapas e não mostre os cálculos intermediários para o estudante, a menos que seja solicitado. Mostre apenas o resultado final formatado no template padrão.

---

## Passo 1: Diagnóstico de Capacidade

Com as informações do estudante (nível, prazo e disponibilidade), calcule:

* **Dias de estudo disponíveis**: conte apenas os dias da semana informados, entre a data de início e o **dia anterior** à data de entrega do projeto.
* **Dias de margem** = 15% dos dias de estudo, arredondado para baixo (mínimo 1). Posicione os dias de margem no **fim das semanas**. Eles não recebem conteúdo novo: servem para ajustar código, resolver bugs não planejados ou fazer revisões.
* **Horas líquidas** = (dias de estudo − dias de margem) × horas por dia.

*Se o prazo tiver menos de 3 dias de estudo, avise que o plano será uma **imersão de entrega rápida** focada estritamente nas 3 funcionalidades core (Adicionar, Concluir, Remover).*

## Passo 2: Decomposição do Desafio (Dev com IA)

1. Quebre o desenvolvimento da aplicação em **4 a 6 módulos progressivos**, respeitando a esteira do desenvolvimento com Google Antigravity:
   - **Módulo 1:** Estrutura e Prompt Inicial (Engenharia de Prompt para criação base).
   - **Módulo 2:** Lógica Fundamental (Inclusão e Remoção de dados).
   - **Módulo 3:** Refatoração & Interface Visual (Estilização condicional CSS/JS).
   - **Módulo 4:** Validação & Testes Automáticos (Execução de testes via Antigravity).
   - **Módulo 5:** Entendimento de Código & Documentação (Feynman do código gerado).
2. Estime as horas considerando o perfil:
   * **Iniciante:** foco maior em entender o código gerado pelo Antigravity e testar manualmente.
   * **Intermediário/Avançado:** foco em otimização do código, arquitetura e testes de regressão.
3. Reserve **20% das horas líquidas para leitura/entendimento do código** e **10% para a validação final por checklist**.

## Passo 3: Distribuição das Sessões e Mapeamento de Prompts

1. Consulte `tecnicas.md` para selecionar a técnica pedagógica de cada sessão.
2. Distribua a construção da aplicação respeitando:
   * **Ritmo de Prompting:** cada sessão deve evoluir o projeto através de um prompt específico enviado ao Google Antigravity.
   * **Revisão de Código (D+1, D+3):** os primeiros 10 a 15 minutos de cada sessão devem focar em explicitar com as próprias palavras o que a IA alterou no código no dia anterior.
   * **Entregável concreto:** toda sessão gera um artefato funcional visível (ex.: layout inicial, função de exclusão ativa, CSS de concluído aplicado).

## Passo 4: Checkpoints Semânticos do Código

No último dia de cada semana (ou módulo principal), inclua um **checkpoint** focado em legibilidade e domínio do código gerado:

* **3 a 5 perguntas de autoavaliação técnica**: sobre como as tecnologias (HTML, CSS e JS) integradas pelo Antigravity conversam entre si.
* **Critério de "dominei"**: o que o estudante deve conseguir fazer sem o auxílio do Antigravity (ex.: "identificar qual função JavaScript é disparada ao clicar no botão de remover").
* **Plano de contingência**: se o estudante não souber explicar a alteração, solicitar ao Antigravity uma explicação simplificada ("modo iniciante") na sessão de margem.

## Passo 5: Montagem da Resposta e Salvamento do CSV

1. Preencha todas as seções do modelo do plano de estudos.
2. Monte a lista de sessões no formato CSV para o Google Agenda.
3. Salve o arquivo em `plano-de-estudos.csv` utilizando a ferramenta `WriteFile`, seguindo rigorosamente as instruções contidas em `salvar_agenda.md`.
4. Exiba no chat a confirmação do arquivo salvo e o caminho retornado.

## Passo 6: Ajustes de Escopo e Replanejamento

Se o estudante relatar problemas ou atrasos durante o desafio:
* **"O código deu erro/bug"**: aloque a sessão seguinte para depuração orientada pelo Antigravity utilizando as técnicas de *AI-assisted Debugging*.
* **"Fiquei sem tempo hoje"**: remaneje a criação do estilo visual para o dia de margem, garantindo que o núcleo funcional (JS) seja mantido intacto.
* **Atualização do CSV**: sempre regravar o arquivo `plano-de-estudos.csv` atualizado após redefinir prazos.