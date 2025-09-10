# Desenvolver o núcleo de um sistema de gerenciamento para uma pequena loja de eletõnicos.
# O sistema precisa gerenciar duas entidade principais. 

import json
produto = []
categoria = []

id_categoria = 0 
id_produto = 0 



def exibir_menu():
    print("-----Loja Descoberta de Tudo-----")
    print("1- Listar o Produto")
    print("2- Cadastrar a Categoria")
    print("3- Listar a Catedoria ")
    print("4- Alterar Produto")
    print("5- Adicionar produto")
    print("6 - Categoria Adicionada")
    print("7 - Sair, até a proxima")

def cadastro():
    nome = input("Nome Da Nova Categoria:")
    novo_id = categoria_id(categoria, "categoria_id")
    novo_categoria = {
        "categoria_id": categoria_id, 
        "nome_categoria" : nome
    }

categoria.append(novo_categoria)
salvar_arquivo(arquivo_categoria , categoria)
categoria_id + = 1


    #-------------------------------------------------------------------
def carregar_categoria():
    try:
        with open(, 'r') as arquivo:
            categoria = json.load(arquivo)
            print("Arquivo carregado!")
except FileNotFoundError:
    print("Arquivo nao encontrado")

def carregar_categorias():
   print ("/cadastrar produto:")
   nome_categoria = input ("nome: ")
   id_categoria +=1 

 categoria_estoque = {
       "nome_categoria" : nome_categorias, 
       "id_categoria" : id_categoria
}

 def cadastrar_produto(): 
       id_produto +=1 
       nome_produto = input ("nome: ")
       preco = input ("preco: ")
       id_categoria_associada = input 

       produto_estoque = {
         "nome_produto" : nome_produto,
         "id_produto" : id_produto,
         "preco" : preco,
         "id_categoria_associada" : id_categoria_associada, 
 }

#--------------------------------------------------------------------

while True:
    try:
        ano_publicacao = int(input("diga o que quer: "))
        break2222222
    except ValueError:
        print("fala só o que quer.")