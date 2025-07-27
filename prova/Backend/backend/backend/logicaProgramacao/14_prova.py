# Atividade 01
# digitar minha idade 

idade = int(input("Digita sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# Atividade 02
# digitar o número inteiro 
numero = int(input("Digite um número inteiro: ")) 

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

    # Atividade 03
    # fazer uma ordem decrescente de número 

for numero in range(10, 0, -1):  
    print(numero) 


    # Atividade 04
    # fazer uma tabuada 

    numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


    # Atividade 05
     # fazer o terminal digitar varias vezez os números e depois chegar num resultado
soma_total = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    soma_total += numero 

print(f"A soma total dos números digitados é: {soma_total}")

# atividade 06 
#criar um número secreto 

numero_secreto = 7
tentativa = None

while tentativa != numero_secreto:
    tentativa = int(input("tentar adivinhar o número que eu escolhi: ")) 
    
    if tentativa < numero_secreto:
        print("Baixo! Tente novamente.") 
    elif tentativa > numero_secreto:
        print("alto! Tente novamente.")
    else:
        print("acertou, joelma do calypson !")


#atividade 07 
        # fazer uma lista de compras 
        
        lista_mercado = ["carambolas", "caju", "abacate" , "mamão lava a outra" , "suco de caju" , "pão de ninho" , "vela"]

print("\nLista Inicial:")
print(*[f"{i+1}. {item}" for i, item in enumerate(lista_mercado)], sep="\n")

while True:
    novo_item = input("\nNovo item (ou 'sair' para encerrar): ").strip()
    
    if novo_item.lower() == 'sair':
        break
        
    if novo_item:
        lista_mercado.append(novo_item)
        print("\nLista Atualizada:")
        print(*[f"{i+1}. {item}" for i, item in enumerate(lista_mercado)], sep="\n")
    else:
        print("digite um item")

print("\nLista Final:", lista_mercado)


#atividade 08 
# Criando uma lista de números inteiros 

numeros = [80, 35, 20, 10, 40, 52, 78, 90, 60, 70]
maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número na lista é: {maior_numero}")