# 📝 Minha Lista de Tarefas - Desafio 3

Este projeto é uma aplicação web simples de Lista de Tarefas (To-Do List), desenvolvida em um único arquivo (`index.html`) utilizando as tecnologias bases da web. O projeto foi construído como parte do Desafio de desenvolvimento (Google Antigravity) para praticar lógica de programação, manipulação visual e interação com o usuário.

## ✨ Funcionalidades

A aplicação cumpre todos os requisitos do desafio, oferecendo as seguintes funcionalidades:

1. **Adicionar Tarefas:** 
   * Digite uma atividade no campo de texto e clique no botão "Adicionar" (ou pressione a tecla *Enter*) para incluí-la na sua lista.
2. **Marcar Tarefas como Concluídas:** 
   * Cada tarefa possui uma caixa de seleção (checkbox). Ao marcá-la, a tarefa ganha um visual diferente (fundo verde claro e texto tachado), ajudando a diferenciar rapidamente o que já foi feito do que ainda está pendente.
3. **Remover Tarefas:** 
   * Se uma atividade não é mais necessária ou foi digitada por engano, basta clicar no botão de exclusão (`✕`) ao lado direito da tarefa para removê-la da lista.

## 🛠️ Tecnologias Utilizadas

Para facilitar o entendimento e focar nos conceitos básicos de desenvolvimento de software, o projeto não utiliza frameworks complexos. Tudo está contido no arquivo `index.html`, dividido em três pilares:

* **HTML5:** Estrutura da página (título, campo de entrada, botões e a lista).
* **CSS3:** Estilização da interface, tornando-a amigável e implementando a melhoria visual das tarefas concluídas (através da classe `.concluida`).
* **JavaScript (Vanilla):** A "inteligência" da aplicação. Responsável por guardar a lista de tarefas na memória, ler o que o usuário digita e atualizar a tela em tempo real sempre que uma ação (adicionar, concluir ou remover) acontece.

## 🧠 Como o código do `index.html` funciona?

Se você abrir o arquivo `index.html` em um editor de código, perceberá as seguintes divisões:

1. **`<style>` (CSS):** Define cores, espaçamentos e o design responsivo. Destaque para o bloco `MELHORIA VISUAL`, onde regras específicas alteram a cor de fundo e o texto das tarefas quando estão completas.
2. **`<body>` (HTML):** Contém os elementos visuais, como o campo `<input>`, o botão `<button>` e a lista `<ul>` vazia que o JavaScript preenche dinamicamente.
3. **`<script>` (JavaScript):** 
   * Mantém um *Array* chamado `tarefas` para armazenar o estado de cada atividade (seu texto e se está concluída ou não).
   * A função `renderizarTarefas()` é o coração visual: ela limpa a lista antiga e desenha a nova lista sempre que o Array é modificado.

## 🚀 Como Executar o Projeto

Como a aplicação roda inteiramente no navegador do cliente (Client-side), não é necessária nenhuma instalação ou configuração de servidor.

1. Faça o download ou salve o arquivo `index.html` no seu computador.
2. Dê um duplo clique no arquivo ou arraste-o para dentro do seu navegador de internet favorito (Google Chrome, Firefox, Edge, etc.).
3. A aplicação estará pronta para uso! Teste adicionar, concluir e remover suas tarefas.

---
*Projeto desenvolvido para fins de estudo de conceitos fundamentais de desenvolvimento de software.*