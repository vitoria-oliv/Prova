def lista_de_convidados():
   
    convidados = []
    print("--- Cadastro de Convidados ---")
    print("Digite o nome de cada convidado. Digite 'fim' para encerrar o cadastro.")

    while True:
        nome_convidado = input("Nome do convidado: ").strip().lower()
        if nome_convidado == 'fim':
            break
        convidados.append(nome_convidado)

    print("\n--- Verificação de Entrada ---")
    while True:
        nome_verificacao = input("Digite seu nome (ou 'sair' para encerrar): ").strip().lower()
        if nome_verificacao == 'sair':
            break
        
        if nome_verificacao in convidados:
            print("Pode entrar. Bem-vindo(a)!")
        else:
            print("Entrada negada. Você não está na lista de convidados.")

if __name__ == "__main__":
    lista_de_convidados()





# Nome do arquivo onde as palavras serão salvas
arquivo_palavras = "palavras.txt"

# Parte 1: Cadastro das palavras
with open(arquivo_palavras, "w") as arquivo:
    print("Cadastro de palavras. Digite 'sair' para encerrar.")
    while True:
        palavra = input("Digite uma palavra: ").strip()
        if palavra.lower() == "sair":
            break
        arquivo.write(palavra + "\n")

# Parte 2: Jogo de adivinhação
# Lê as palavras do arquivo
with open(arquivo_palavras, "r") as arquivo:
    lista_palavras = [linha.strip().lower() for linha in arquivo]

# Início do jogo
print("\nJogo de adivinhação! Tente adivinhar uma palavra cadastrada.")

while True:
    tentativa = input("Digite sua tentativa (ou 'sair' para encerrar): ").strip().lower()
    if tentativa == "sair":
        print("Jogo encerrado.")
        break
    if tentativa in lista_palavras:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Tente novamente.")