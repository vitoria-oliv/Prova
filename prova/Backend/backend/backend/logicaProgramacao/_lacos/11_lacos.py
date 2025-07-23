soma_total = 0.0  # Variável para armazenar a soma total dos valores

print("Bem-vindo(a) à Calculadora de Soma Flexível!")
print("Digite um número para adicioná-lo à soma.")
print("Para subtrair, digite um número negativo.")
print("Digite 0 (zero) para encerrar e ver o resultado final.")

while True:
    try:
        valor = float(input("Digite um valor (ou 0 para sair): "))

        if valor == 0:
            print("\nEncerrando o programa...")
            print(f"A soma final de todos os valores é: R$ {soma_total:.2f}")
            break  # Sai do laço de repetição

        elif valor > 0:
            soma_total += valor  # Soma o valor ao total
            print(f"Valor adicionado. Soma parcial: R$ {soma_total:.2f}")
        else: # valor < 0
            soma_total += valor  # Subtrai o valor (adiciona um negativo)
            print(f"Valor subtraído. Soma parcial: R$ {soma_total:.2f}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")