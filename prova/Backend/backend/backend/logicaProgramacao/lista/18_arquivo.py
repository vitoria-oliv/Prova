#------LISTA DE COMPRAS -------
#def gerar_lista_compras():
    #print("Seja bem-vindo, vamos as compras")
   # print("Ao encerrar digite Fim")
   
   # with open("comida.txt" , 'w') as comida:
      # while True:
           # item = input("Digite o item: ")
            #if item.lower()=="fim":
                #print("encerrando lista")
                #break    
            #comida.write(item + "\n")

#gerar_lista_compras()

#-------- LISTA DE ITENS -------
#def listar_itens():
 #with open("comida.txt", 'r') as listas:
  # print("----Listas De Compras----")
   #for item in listas:
    #produto = item.strip()
    #rint("item:",produto)
#listar_itens()

# ----- ARQUIVO DE CHAMADA -----


    def gerar_lista_alunos():
    print("Seja bem-vindo, vamos cadastrar os alunos")
    print("Ao encerrar digite encerrar")
   
    with open("terceirao.txt", 'w') as arquivo:
        while True:
            nome = input("Digite o nome do aluno: ")
            if nome.lower() == "encerrar":
                print("Encerrando lista...")
                break    
            arquivo.write(nome + "\n")

gerar_lista_alunos()

def listar_alunos():
    with open("terceirao.txt", 'r') as arquivo:
        print("---- Lista de Alunos ----")
        for linha in arquivo:
            aluno = linha.strip()
            print("aluno", aluno)

listar_alunos()