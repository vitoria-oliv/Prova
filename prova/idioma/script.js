// script.js
const vocabulario = [
    {portugues: 'gato', ingles: 'cat'},
    {portugues: 'cachorro', ingles: 'dog'},
    {portugues: 'maçã', ingles: 'apple'},
    {portugues: 'livro', ingles: 'book'},
    {portugues: 'amor', ingles: 'love'}
];

let pontuacao = 0;
let perguntaAtual = {};
let opcoes = [];

function proximaPergunta() {
    document.getElementById('resultado').textContent = '';
    
    perguntaAtual = vocabulario[Math.floor(Math.random() * vocabulario.length)];
    document.getElementById('palavra').textContent = `Tradução de: "${perguntaAtual.portugues}"`;
    
    opcoes = [perguntaAtual.ingles];
    
    while (opcoes.length < 4) {
        let aleatoria = vocabulario[Math.floor(Math.random() * vocabulario.length)].ingles;
        if (!opcoes.includes(aleatoria)) {
            opcoes.push(aleatoria);
        }
    }
    
    opcoes.sort(() => Math.random() - 0.5);
    
    const opcoesDiv = document.getElementById('opcoes');
    opcoesDiv.innerHTML = '';
    
    opcoes.forEach(opcao => {
        const btn = document.createElement('button');
        btn.textContent = opcao;
        btn.className = 'opcao';
        btn.onclick = () => verificarResposta(opcao);
        opcoesDiv.appendChild(btn);
    });
}

function verificarResposta(resposta) {
    if (resposta === perguntaAtual.ingles) {
        document.getElementById('resultado').textContent = '✅ Correto!';
        pontuacao++;
    } else {
        document.getElementById('resultado').textContent = `❌ Errado! Correto: ${perguntaAtual.ingles}`;
    }
    document.getElementById('pontuacao').textContent = pontuacao;
}

// Iniciar o quiz ao carregar a página
window.onload = proximaPergunta;