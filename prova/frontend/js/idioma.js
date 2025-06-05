// script.js

// Variável que armazena o progresso do usuário
let progresso = 0;

/**
 * Atualiza visualmente o progresso do usuário na interface
 */
function atualizarProgresso() {
  const progressoEl = document.getElementById('progresso');
  if (progressoEl) {
    progressoEl.textContent = `Progresso: ${progresso}%`;
  }
}

/**
 * Gera recomendações personalizadas com base no progresso
 */
function recomendarConteudo() {
  const recomendacaoEl = document.getElementById('recomendacao');
  if (!recomendacaoEl) return;

  if (progresso < 30) {
    recomendacaoEl.textContent = "Recomendamos começar pelos vídeos culturais!";
  } else if (progresso < 70) {
    recomendacaoEl.textContent = "Experimente os quizzes e jogos interativos!";
  } else {
    recomendacaoEl.textContent = "Participe do fórum para praticar com falantes nativos!";
  }
}

/**
 * Inicia o quiz interativo
 */
function iniciarQuiz() {
  const resposta = prompt("Qual é a capital da França?");
  
  if (!resposta) {
    alert("Por favor, insira uma resposta.");
    return;
  }

  if (resposta.trim().toLowerCase() === "paris") {
    alert("Correto! +10% de progresso.");
    progresso = Math.min(progresso + 10, 100);
  } else {
    alert("Incorreto. Tente novamente mais tarde.");
  }

  atualizarProgresso();
  recomendarConteudo();
}

/**
 * Configura os eventos ao carregar a página
 */
function inicializarAplicacao() {
  atualizarProgresso();
  recomendarConteudo();

  const botaoQuiz = document.getElementById('botaoQuiz');
  if (botaoQuiz) {
    botaoQuiz.addEventListener('click', iniciarQuiz);
  }
}

// Evento de inicialização
document.addEventListener('DOMContentLoaded', inicializarAplicacao);