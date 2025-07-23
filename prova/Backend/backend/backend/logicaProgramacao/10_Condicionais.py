salario = float(input("Digite seu Salario:"))

salario_mensal = float (input("digite seu salario mensal :"))

# calculando o salario * 12
 
salario_anual = salario_mensal * 12

print(f"seu salario anual é: R$ {salario_anual}")

if(salario >= 5000):
   imposto = salario * 12 / 100
   print("imposto é:" , imposto)

elif(salario >= 2000):
    imposto = salario * 7 / 100
    print("imposto é" , imposto)

else:
    imposto = salario * 3 / 100
    print("imposto é" , imposto)

imposto_anual = imposto * 12
print(f"seu imposto anual é: R${imposto_anual}")        