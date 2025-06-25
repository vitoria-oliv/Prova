def contar_ate_dez():
  for i in range(1, 11): 
    print(i)
contar_ate_dez()


def imprimir_nome_varias_vezes(nome, numero):
  for i in range(numero):
    print(nome)

imprimir_nome_varias_vezes("joelma do para", 5)

print("\n--- Próximo exemplo ---\n")

imprimir_nome_varias_vezes("gigi canivete", 3)


def somar_cinco_numeros():
  total = 0
  for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    total += numero
  print("Total:", total)

somar_cinco_numeros()




def imprimir_tabuada(numero):
  
  print(f"--- Tabuada do {numero} ---")
  for i in range(1, 11): # Gera números de 1 a 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

imprimir_tabuada(2)
imprimir_tabuada(5)
imprimir_tabuada(3)





def mostrar_numeros_pares():

  print("Números pares entre 1 e 20:")
  for i in range(2, 21, 2): # Começa em 2, vai até 20 (não incluindo 21), pulando de 2 em 2
    print(i)

# Exemplo de uso da função:
mostrar_numeros_pares()