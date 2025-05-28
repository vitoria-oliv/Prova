idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você **não** pode votar.")

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior.")
elif numero2 > numero1:
    print("O segundo número é maior.")
else:
    print("Os dois números são iguais.")
