// 1. QUIZ INTERATIVO
document.addEventListener("DOMContentLoaded", () => {
  const quizBtn = document.querySelector("#iniciar-quiz");
  if (quizBtn) {
    quizBtn.addEventListener("click", iniciarQuiz);
  }
});

function iniciarQuiz() {
  const pergunta = "O que significa 'Bonjour' em francês?";
  const respostaUsuario = prompt(pergunta + "\nA) Olá\nB) Obrigado\nC) Adeus");
  const respostaCerta = "A";

  if (respostaUsuario && respostaUsuario.toUpperCase() === respostaCerta) {
    alert("Correto! 'Bonjour' significa 'Olá'.");
    atualizarProgresso(10);
  } else {
    alert("Resposta incorreta. A resposta certa é: A) Olá.");
  }
}

// 2. RASTREAMENTO DE PROGRESSO (com localStorage)
function atualizarProgresso(pontos) {
  let progressoAtual = parseInt(localStorage.getItem("progresso")) || 0;
  progressoAtual += pontos;
  localStorage.setItem("progresso", progressoAtual);
  mostrarProgresso();
}

function mostrarProgresso() {
  const barra = document.querySelector("#progresso");
  if (barra) {
    const progresso = parseInt(localStorage.getItem("progresso")) || 0;
    barra.style.width = Math.min(progresso, 100) + "%";
    barra.innerText = progresso + "%";
  }
}

// 3. RECOMENDAÇÃO SIMPLES DE CONTEÚDO
function recomendarConteudo() {
  const recomendacoes = [
    "Ouça um podcast sobre a culinária francesa.",
    "Assista a um vídeo sobre o Louvre.",
    "Leia um artigo sobre expressões francesas.",
    "Explore uma música tradicional francesa."
  ];

  const indice = Math.floor(Math.random() * recomendacoes.length);
  alert("Recomendação cultural de hoje:\n" + recomendacoes[indice]);
}

document.addEventListener("DOMContentLoaded", () => {
  mostrarProgresso();

  const btnRecomendar = document.querySelector("#recomendar");
  if (btnRecomendar) {
    btnRecomendar.addEventListener("click", recomendarConteudo);
  }
});