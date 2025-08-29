import json
inventario = []

try: 
    with open ('loja.json' , 'r') as arquivo:
        inventario = json.load(arquivo)
        print("arquivo carregado !")
except  FileNotFoundError:
    print("arquivo não encontrado")

print("\n ----Cadastrar Produto----")
    
novo_produto = input("digite o nome do produto:")
while True:
    try:
        quantidade = int (input("digite a quantidade"))
        break; 
    except ValueError:
        print("digite apenas números")

while True :
    try :
        preco = float(input("digite o preço"))
        break; 
    except ValueError :
        print("digite o preço corre")          

novo_produto = {"novo_produto": novo_produto , 
                "quantidade": quantidade , 
                "preco": preco ,
                "tem_estoque": quantidade > 0 }           

#escrever no arquivo json 

inventario.append(novo_produto) 
with open ('loja.json' , 'w') as arquivo:
    json.dump(inventario, arquivo, indent = 4)
print(f"\n produto {novo_produto} foi cadastrado")