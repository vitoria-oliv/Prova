# Desenvolver o núcleo de um sistema de gerenciamento para uma pequena loja de eletõnicos.
# O sistema precisa gerenciar duas entidade principais. 
# ATIVIDADE AVALIATIVA 

import json

ARQUIVO_CATEGORIAS = 'categorias.json'
ARQUIVO_PRODUTOS = 'produtos.json'

categorias_id = 0
produtos_id = 0

categorias = []
produtos = []

def carregar_arquivo(categorias):
    try:
        with open(categorias, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_arquivo(nome, dados):
    with open(nome, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def exibir_menu():
    print("\n- Loja a Descoberta de Tudo -")
    print("1 -- Cadastrar categoria")
    print("2 -- Cadastrar produto")
    print("3 -- Listar categorias")
    print("4 -- Listar produtos")
    print("5 -- Sair")

def cadastrar_categoria():
    global categorias_id
    global categorias
    
    nome_categoria = input("Nome da categoria: ")
    categoria = {"id": categorias_id, "nome": nome_categoria}
    categorias.append(categoria)
    salvar_arquivo(ARQUIVO_CATEGORIAS, categorias)
    categorias_id += 1

    print("Categoria cadastrada!")

def cadastrar_produto():
    global produtos_id
    global produtos
    
    nome_produto = input("Nome do produto: ")
    preco = float(input("Preço: "))
    id_categoria = int(input("ID da categoria: "))
    produto = {
        "id": produtos_id,
        "nome": nome_produto,
        "preco": preco,
        "id_categoria": id_categoria
    }
    produtos.append(produto)
    salvar_arquivo(ARQUIVO_PRODUTOS, produtos)
    produtos_id += 1

    print("Produto cadastrado!")

def listar_categorias():
    global categorias
    if categorias:
        print("CATEGORIAS:")
        for categorias in categorias:
            print(f"ID: {categorias['id']} - Nome: {categorias['nome']}")
    else:
        print("Nenhuma categoria cadastrada.")

def listar_produtos():
    global produtos
    global categorias
    if produtos:
        print("PRODUTOS:")
        for produtos in produtos:
            print(f"ID: {produtos['id']} - Nome: {produtos['nome']} - Preço: {produtos['preco']} - Categoria: {produtos['id_categoria']}") 
    else:
        print("Nenhum produto cadastrado.")

categorias = carregar_arquivo(ARQUIVO_CATEGORIAS)
produtos = carregar_arquivo(ARQUIVO_PRODUTOS)

while True:
    exibir_menu()
    opcao = input("Escolha o número: ")

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        cadastrar_produto()
    if opcao == '3':
        listar_categorias()
    elif opcao == '4':
        listar_produtos()
    elif opcao == '5':
        print("Saindo... Até a proxima!")
        break
    else:
        print("Opção inválida.")