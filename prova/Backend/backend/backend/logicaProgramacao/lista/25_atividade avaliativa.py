# Desenvolver o núcleo de um sistema de gerenciamento para uma pequena loja de eletõnicos.
# O sistema precisa gerenciar duas entidade principais. 
# ATIVIDADE AVALIATIVA 

import json


arquivo_Produto = "produtos.json"
id_counter = 0

def carregarProdutos():
    "Carrega os produtos de um arquivo JSON. Se o arquivo não existir, retorna uma lista vazia."
    return json.load(open(arquivo_Produto, "r")) if os.path.exists(arquivo_Produto) else []

def salvarProdutos(produtos):
    "Salva os produtos em um arquivo JSON de forma organizada."
    json.dump(produtos, open(arquivo_Produto, "w"), indent=2, ensure_ascii=False)

def cadastrarProduto():
    global id_counter
    produtos = carregarProdutos()

    print("\n--- Cadastro de Produto ---")
    
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Nome do produto não pode ser vazio.")
        input("Pressione Enter para continuar...")
        return
        
    try:
        preco_str = input("Digite o valor do produto: ").replace(",", ".")
        preco = float(preco_str)
    except ValueError:
        print("Preço inválido. Por favor, digite um número.")
        input("Pressione Enter para continuar...")
        return

    id_counter += 1
    novo_produto = {"id": id_counter, "nome": nome, "preco": preco}
    
    produtos.append(novo_produto)
    salvarProdutos(produtos)
    
    print(f"\nProduto cadastrado: ID: {id_counter} | Nome: {nome} | Preço: R$ {preco:.2f}")

def listaProdutos():
    produtos = carregarProdutos()
    
    if not produtos:
        print("\nNenhum produto cadastrado.")
    else:
        print("\n----- Produtos -----")
        for p in produtos:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: R$ {p['preco']:.2f}")

def MenuPrincipal():
    while True:
        funcao = input("\n--- Loja a Descoberta de Tudo ---\n1. Cadastrar novo produto\n2. Listar Produtos\n3. Sair\nOpção: ")
        
        match funcao:
            case "1":
                cadastrarProduto()
            case "2":
                listaProdutos()
            case "3":
                print("\nSaindo...")
                break
            case _:
                print("\nOpção inválida, tente novamente.")
MenuPrincipal()