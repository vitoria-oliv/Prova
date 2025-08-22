#Quando estamos aprendendo Python, um dos maiores desafios é entender como lidar com erros que ocorrem durante a execução do programa.
#Felizmente, a linguagem oferece mecanismos poderosos para capturar e tratar esses erros, como o uso dos blocos try e except.
#Exceptions em Python são erros que ocorrem durante a execução de um programa, sendo usadas para sinalizar situações excepcionais que podem interromper o fluxo normal do código.
#A principal forma de tratar esses erros é utilizando os blocos try except.

def cadastrar():
    try:
        arq = open("usuarios.txt", "a")
        nome = input("Nome: ")
        email = input("Email: ")
        arq.write(nome + "," + email + "\n")
        arq.close()
        print("Usuário cadastrado!")
    except:
        print("Erro ao cadastrar usuário.")


def listar():
    try:
        arq = open("usuarios.txt", "r")
        print("\n--- Usuários cadastrados ---")
        for linha in arq:
            print(linha.strip())
        arq.close()
    except:
        print("Nenhum usuário encontrado.")


def alterar():
    try:
        nome_antigo = input("Digite o nome que deseja alterar: ")
        arq = open("usuarios.txt", "r")
        usuarios = arq.readlines()
        arq.close()

        arq = open("usuarios.txt", "w")
        achou = False
        for u in usuarios:
            nome, email = u.strip().split(",")
            if nome == nome_antigo:
                novo_nome = input("Novo nome: ")
                novo_email = input("Novo email: ")
                arq.write(novo_nome + "," + novo_email + "\n")
                achou = True
                print("Usuário alterado!")
            else:
                arq.write(u)
        arq.close()
        if not achou:
            print("Usuário não encontrado.")
    except:
        print("Erro ao alterar usuário.")


def excluir():
    try:
        nome_excluir = input("Digite o nome que deseja excluir: ")
        arq = open("usuarios.txt", "r")
        usuarios = arq.readlines()
        arq.close()

        arq = open("usuarios.txt", "w")
        achou = False
        for u in usuarios:
            nome, email = u.strip().split(",")
            if nome == nome_excluir:
                achou = True
                print("Usuário excluído!")
            else:
                arq.write(u)
        arq.close()
        if not achou:
            print("Usuário não encontrado.")
    except:
        print("Erro ao excluir usuário.")


# Menu principal
while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Alterar usuário")
    print("4 - Excluir usuário")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")