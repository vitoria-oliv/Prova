#exercicio para praticar json 
#contexto: a biblioteca precisa de um sistema para catalogar os livros da esola 
#crie um sistema que salve e liste os livros que devem ser salvos no arquivo biblioteca.json
#atributos necessarios 
#titulo 
#autor
#editora
#ano_publicacao
#genero
#numero_paginas
#idioma

import json 

livros = []
try:
    with open('biblioteca.json', 'r') as arquivo:
        livros = json.load(arquivo)
        print("Arquivo carregado!")
except FileNotFoundError:
    print("Arquivo nao encontrado")

print("\n---- Cadastrar livro ----")
titulo = input("Digite o título do livro: ")

autor = input("Digite o nome do autor: ")

editora = input("Digite a editora: ")

while True:
    try:
        ano_publicacao = int(input("Digite o ano de publicação: "))
        break
    except ValueError:
        print("Digite apenas numeros para o ano.")

while True:
    try:  
        numero_paginas = int(input("Digite o número de páginas: ")) 
        break
    except ValueError:
        print("Digite apenas numeros para páginas.")

genero = input("Digite o gênero: ")
idioma = input("Digite o idioma: ")

novo_livro = {
    "titulo": titulo,
    "autor": autor,
    "editora": editora,
    "ano_publicacao": ano_publicacao,
    "genero": genero,
    "numero_paginas": numero_paginas,
    "idioma": idioma
}

livros.append(novo_livro)
with open('biblioteca.json', 'w') as arquivo:
    json.dump(livros, arquivo, indent=4)

print(f"\nLivro '{titulo}' foi cadastrado com sucesso.")




# i = 0 
# i ++ -------- i = i + 1
# Auto incremento = Automático 
 
 # inventario = []
 # with open ("biblioteca.json" , "r") as biblioteca:
   # produto_para_alterar = int(input("digite o id do produto"))]
   # inventario = json.load (biblioteca)
   # for livro in inventario:
   # if produto_para_alterar == livro ["id"]:
    # novo_nome = input("digite seu nome")
     # livro["nome"] = novo_nome
# with open ("biblioteca.json" , "w") as biblioteca:
   #json.dump (inventario, biblioteca, indent = 4)
   #remover o arquivo
     
     #---------------------------------------------------------

     # inventario = []
 # with open ("biblioteca.json" , "r") as biblioteca:

   # livro_para_excluir = int(input("digite o id do livro"))]
   # inventario = json.load (biblioteca)
   # for livro in inventario:
    
    # for livro in inventario = []
    # if livro_para_excluir ! = livro ["id"]:
    # novo_inventario.append(livro)

# with open ("biblioteca.json" , "w") as biblioteca:
   #json.dump (inventario, biblioteca, indent = 4)   