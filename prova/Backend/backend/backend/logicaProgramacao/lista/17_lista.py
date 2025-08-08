#lista de compras 
# Lista de produtos
produtos = []

def cadastrar_produto(produto):
    produtos.append(produto)
    print(f"Produto '{produto}' cadastrado com sucesso.")

def excluir_produto(produto):
    if produto in produtos:
        produtos.remove(produto)
        print(f"Produto '{produto}' excluído com sucesso.")
    else:
        print(f"Produto '{produto}' não encontrado.")

def listar_produtos():
    if produtos:
        print("Lista de produtos:")
        for produto in produtos:
            print(f"- {produto}")
    else:
        print("Nenhum produto cadastrado.")

# Menu de operações
while True:
    print("\nMENU DE OPERAÇÕES")
    print("1. Cadastrar produto")
    print("2. Excluir produto")
    print("3. Listar produtos")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")
    
    match opcao:
        case "1":
            produto = input("Digite o nome do produto a ser cadastrado: ")
            cadastrar_produto(produto)
        case "2":
            produto = input("Digite o nome do produto a ser excluído: ")
            excluir_produto(produto)
        case "3":
            listar_produtos()
        case "4":
            print("Saindo do programa.")
            break
        case _:
            print("Opção inválida. Tente novamente.")