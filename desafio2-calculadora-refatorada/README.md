# 🚀 Calculadora Refatorada (+ Testes)

![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen?style=for-the-badge)
![Nível](https://img.shields.io/badge/nível-intermediário-orange?style=for-the-badge)

Evolução da calculadora de linha de comando inicial, implementando uma nova funcionalidade (cálculo de porcentagem) e garantindo a integridade do sistema através de testes simulados via script.

---

## 📌 Sobre o Projeto

Este projeto faz parte do **Desafio 02** da Imersão Dev na Era da IA. O objetivo principal foi vivenciar o dia a dia de um Engenheiro de Software: analisar uma base de código existente (Desafio 01), planejar a inserção de uma nova *feature* com o menor impacto possível na arquitetura atual, e validar a alteração através de testes de regressão.

---

## ✨ Novas Funcionalidades e Melhorias

- [x] **Operação de Porcentagem (`%`)**: Nova opção adicionada ao menu interativo para calcular percentuais.
- [x] **Refatoração do Dispatcher**: Atualização da cadeia `if/elif/else` e da tupla de validação de entradas para acomodar a nova opção sem quebrar o fluxo.
- [x] **Testes Automatizados (Mock)**: Criação de um script de teste estruturado com `mock_input` e `mock_print` para simular a interação do usuário no terminal de forma autônoma.

---

## 🧠 Conceitos Praticados

- **Refatoração de Código**: Alteração de um sistema existente mantendo sua estabilidade.
- **Testes de Regressão**: Validação de operações antigas (ex: adição e divisão por zero) para garantir que a nova funcionalidade não inseriu bugs no legado.
- **Engenharia de Prompt (Método GCCD)**: Uso estruturado do Google AI Studio fornecendo Objetivo, Contexto, Restrições e Critérios de Conclusão para guiar a IA na geração dos testes.

---

## 💻 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o [Python 3](https://www.python.org/) instalado em seu computador.

### Passo a passo

1. **Clone o repositório**:
   ```bash
   git clone [https://github.com/fernandoYepes/Imersao-Dev-IA-Alura-Google.git](https://github.com/fernandoYepes/Imersao-Dev-IA-Alura-Google.git)