# eu como um dono de concessionaria de carros importados, preciso de um sistema
# para controlar meu estoque de veiculos. para me organizar melhor
# além do nome gostaria de guardar o ano, quilometragem, marca, preço, cor e quantidade de cada veiculo
#quero um menu, onde eu possa cadastrar, alterar, excluir e listar meus veiculos. para me sentir especial
#quero o nome da minha loja apareça no topo do menu
#moya´s imports

# Lista para armazenar o estoque de veículos.

import json
import os

# Nome do arquivo JSON que armazenará os dados do estoque
ARQUIVO_ESTOQUE = "estoque_moys_imports.json"

def carregar_estoque():
    """Carrega o estoque do arquivo JSON."""
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, "r") as arquivo:
            return json.load(arquivo)
    return []

def salvar_estoque(estoque):
    """Salva o estoque no arquivo JSON."""
    with open(ARQUIVO_ESTOQUE, "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_veiculos(estoque):
    """Lista todos os veículos no estoque."""
    limpar_tela()
    if not estoque:
        print("Nenhum veículo cadastrado no estoque.")
    else:
        print("--- Lista de Veículos ---")
        for veiculo in estoque:
            print(f"\nID: {veiculo['id']}")
            print(f"Nome: {veiculo['nome']}")
            print(f"Marca: {veiculo['marca']}")
            print(f"Ano: {veiculo['ano']}")
            print(f"Cor: {veiculo['cor']}")
            print(f"Quilometragem: {veiculo['quilometragem']} km")
            print(f"Preço: R$ {veiculo['preco']:.2f}")
            print(f"Quantidade: {veiculo['quantidade']}")
        print("\n-------------------------")

def cadastrar_veiculo(estoque):
    """Cadastra um novo veículo."""
    limpar_tela()
    print("--- Cadastrar Novo Veículo ---")
    
    # Gera um ID único para o novo veículo
    proximo_id = 1
    if estoque:
        proximo_id = max(v['id'] for v in estoque) + 1
        
    nome = input("Nome do veículo: ")
    marca = input("Marca: ")
    ano = int(input("Ano: "))
    cor = input("Cor: ")
    quilometragem = float(input("Quilometragem: "))
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade em estoque: "))

    novo_veiculo = {
        'id': proximo_id,
        'nome': nome,
        'marca': marca,
        'ano': ano,
        'cor': cor,
        'quilometragem': quilometragem,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque.append(novo_veiculo)
    salvar_estoque(estoque)
    print("\nVeículo cadastrado com sucesso!")

def alterar_veiculo(estoque):
    """Altera dados de um veículo existente."""
    listar_veiculos(estoque)
    if not estoque:
        input("\nPressione Enter para continuar...")
        return
    
    try:
        veiculo_id = int(input("\nDigite o ID do veículo que deseja alterar: "))
        
        encontrado = False
        for veiculo in estoque:
            if veiculo['id'] == veiculo_id:
                print(f"\n--- Alterando Veículo (ID: {veiculo_id}) ---")
                
                veiculo['nome'] = input(f"Nome atual ({veiculo['nome']}): ") or veiculo['nome']
                veiculo['marca'] = input(f"Marca atual ({veiculo['marca']}): ") or veiculo['marca']
                veiculo['ano'] = int(input(f"Ano atual ({veiculo['ano']}): ") or veiculo['ano'])
                veiculo['cor'] = input(f"Cor atual ({veiculo['cor']}): ") or veiculo['cor']
                veiculo['quilometragem'] = float(input(f"Quilometragem atual ({veiculo['quilometragem']}): ") or veiculo['quilometragem'])
                veiculo['preco'] = float(input(f"Preço atual ({veiculo['preco']}): ") or veiculo['preco'])
                veiculo['quantidade'] = int(input(f"Quantidade atual ({veiculo['quantidade']}): ") or veiculo['quantidade'])

                salvar_estoque(estoque)
                print("\nDados do veículo alterados com sucesso!")
                encontrado = True
                break
        
        if not encontrado:
            print("ID inválido. Tente novamente.")
    except (ValueError, IndexError):
        print("Entrada inválida. Certifique-se de digitar um número válido.")

def excluir_veiculo(estoque):
    """Exclui um veículo do estoque."""
    listar_veiculos(estoque)
    if not estoque:
        input("\nPressione Enter para continuar...")
        return
    
    try:
        veiculo_id = int(input("\nDigite o ID do veículo que deseja excluir: "))
        
        novo_estoque = []
        veiculo_removido = None
        for veiculo in estoque:
            if veiculo['id'] != veiculo_id:
                novo_estoque.append(veiculo)
            else:
                veiculo_removido = veiculo
        
        if veiculo_removido:
            salvar_estoque(novo_estoque)
            print(f"\nVeículo '{veiculo_removido['nome']}' excluído com sucesso.")
        else:
            print("ID inválido. Tente novamente.")
    except (ValueError, IndexError):
        print("Entrada inválida. Certifique-se de digitar um número válido.")

def menu_principal():
    """Exibe o menu principal e gerencia as opções."""
    estoque = carregar_estoque()
    while True:
        limpar_tela()
        print("=============================")
        print("   Moya's Imports - Sistema de Estoque")
        print("=============================")
        print("\nMenu Principal:")
        print("1. Cadastrar Veículo")
        print("2. Alterar Veículo")
        print("3. Excluir Veículo")
        print("4. Listar Veículos")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            cadastrar_veiculo(estoque)
        elif opcao == '2':
            alterar_veiculo(estoque)
        elif opcao == '3':
            excluir_veiculo(estoque)
        elif opcao == '4':
            listar_veiculos(estoque)
        elif opcao == '5':
            print("Saindo do sistema. Até logo, Moya's Imports!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        input("\nPressione Enter para continuar...")

# Executa o menu principal quando o script é iniciado
if __name__ == "__main__":
    menu_principal()

