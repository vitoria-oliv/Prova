// Garante que o código JavaScript seja executado somente após o carregamento completo do DOM (Document Object Model)
document.addEventListener('DOMContentLoaded', () => {
    // Seleciona os elementos HTML que serão manipulados
    const idiomaOpcoes = document.querySelector('.idioma-opcoes');
    const conteudoIdiomaDiv = document.getElementById('conteudo-idioma');
    const filtroConteudo = document.querySelector('.filtro-conteudo');
    const listaConteudoDiv = document.getElementById('lista-conteudo');
    const secoesMain = document.querySelectorAll('main > section'); // Seleciona todas as seções dentro do <main>
    const navLinks = document.querySelectorAll('nav a'); // Seleciona todos os links de navegação

    // --- Interação para Escolha de Idioma ---
    if (idiomaOpcoes) {
        // Adiciona um ouvinte de eventos para cliques nos botões de idioma
        idiomaOpcoes.addEventListener('click', (event) => {
            // Verifica se o elemento clicado é um botão
            if (event.target.tagName === 'BUTTON') {
                // Obtém o idioma selecionado do atributo 'data-idioma' do botão
                const idiomaSelecionado = event.target.dataset.idioma;
                // Chama a função para carregar o conteúdo específico do idioma
                carregarConteudoIdioma(idiomaSelecionado);
                // Esconde a seção de seleção de idiomas
                document.getElementById('idiomas').classList.add('hidden');
                // Mostra a seção de conteúdo do idioma
                conteudoIdiomaDiv.classList.remove('hidden');
            }
        });
    }

    // Função para simular o carregamento de conteúdo do idioma
    function carregarConteudoIdioma(idioma) {
        // Simulação de dados que viriam do backend
        const conteudoExemplo = {
            espanhol: `<h2 class="idioma-titulo">Aprendendo Espanhol</h2>
                       <p>Descubra a beleza da língua espanhola através de sua cultura vibrante.</p>
                       <button class="botao-quiz" onclick="carregarQuiz('espanhol')">Fazer um Quiz de Espanhol</button>
                       <button onclick="mostrarSecao('conteudo-cultural')">Explorar Conteúdo Cultural em Espanhol</button>`,
            frances: `<h2 class="idioma-titulo">Explorando o Francês</h2>
                      <p>Mergulhe na elegância da língua francesa e sua rica história.</p>
                      <button class="botao-quiz" onclick="carregarQuiz('frances')">Fazer um Quiz de Francês</button>
                      <button onclick="mostrarSecao('conteudo-cultural')">Explorar Conteúdo Cultural em Francês</button>`,
            italiano: `<h2 class="idioma-titulo">A Paixão do Italiano</h2>
                       <p>Sinta a melodia da língua italiana e sua arte inspiradora.</p>
                       <button class="botao-quiz" onclick="carregarQuiz('italiano')">Fazer um Quiz de Italiano</button>
                       <button onclick="mostrarSecao('conteudo-cultural')">Explorar Conteúdo Cultural em Italiano</button>`
        };

        // Atualiza o conteúdo da div com base no idioma selecionado
        conteudoIdiomaDiv.innerHTML = conteudoExemplo[idioma] || `<p>Conteúdo para ${idioma} ainda não disponível.</p>`;
    }

    // --- Interação para Filtrar Conteúdo Cultural ---
    if (filtroConteudo) {
        // Adiciona um ouvinte de eventos para cliques nos botões de filtro de conteúdo
        filtroConteudo.addEventListener('click', (event) => {
            // Verifica se o elemento clicado é um botão
            if (event.target.tagName === 'BUTTON') {
                // Obtém o tipo de conteúdo selecionado do atributo 'data-tipo' do botão
                const tipoConteudo = event.target.dataset.tipo;
                // Chama a função para filtrar e exibir o conteúdo cultural
                filtrarConteudoCultural(tipoConteudo);
            }
        });
    }

    // Função para simular a filtragem de conteúdo cultural
    function filtrarConteudoCultural(tipo) {
        // Simulação de dados de conteúdo cultural (isso viria do backend)
        const conteudos = [
            { tipo: 'video', titulo: 'Cultura Espanhola: La Fiesta', url: '89' },
            { tipo: 'musica', titulo: 'Música Flamenca Autêntica', url: '97' },
            { tipo: 'podcast', titulo: 'História da Arte Francesa', url: '#' },
            { tipo: 'artigo', titulo: 'A Gastronomia Regional Italiana', url: '#' },
            { tipo: 'video', titulo: 'Pontos Turísticos da Itália', url: '#' },
            { tipo: 'musica', titulo: 'Clássicos da Chanson Française', url: '#' },
            { tipo: 'podcast', titulo: 'A Influência da Cultura Espanhola na América Latina', url: '#' },
            { tipo: 'artigo', titulo: 'Curiosidades da Língua Francesa', url: '#' }
            // ... mais conteúdos
        ];

        // Filtra os conteúdos com base no tipo selecionado
        const conteudosFiltrados = conteudos.filter(item => item.tipo === tipo);
        // Chama a função para exibir os conteúdos filtrados
        exibirConteudos(conteudosFiltrados);
    }

    // Função para exibir a lista de conteúdos na tela
    function exibirConteudos(lista) {
        // Cria a estrutura HTML para a lista de conteúdos
            const listaHTML = '<ul>' + lista.map(item => `<li><a href="${item}
