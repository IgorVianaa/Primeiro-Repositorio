"""
Este programa é um sistema de gerenciamento de restaurantes.

Funcionalidades principais:
- Exibição do Programa: Mostra um banner com o nome do programa.
- Cadastro de Restaurantes: Permite ao usuário cadastrar novos restaurantes, especificando o nome, categoria e se o restaurante está ativo ou inativo.
- Listagem de Restaurantes: Exibe todos os restaurantes cadastrados, mostrando o nome, a categoria e o status (ativo ou inativo).
- Ativação/Desativação de Restaurantes: Permite alterar o status de um restaurante entre ativo e inativo.
- Menu Principal: Fornece um menu interativo para o usuário escolher entre as diferentes funcionalidades.

Estrutura do Código:
- Função `exibir_programa()`:Exibe o banner do programa.
- Função `cadastrar_restaurante()`: Adiciona um novo restaurante à lista.
- Função `listar_restaurante()`: Mostra todos os restaurantes cadastrados.
- Função `ativar_desativar_restaurante()`: Permite alterar o status de um restaurante.
- Função `menu()`: Apresenta um menu para navegação e seleção de opções.
- Função `main()`: Inicia o programa, exibindo o banner e chamando o menu principal.

Componentes Utilizados:
- Biblioteca `os`: Usada para limpar a tela do terminal.
- Lista `restaurantes`: Armazena as informações dos restaurantes cadastrados.
- Estruturas de Controle:
  - Loop `while` para manter o programa em execução.
  - Loop `for` para iterar sobre a lista de restaurantes.
  - Estrutura `match-case` para lidar com as opções do menu.
  - Bloco `try-except` para tratar entradas inválidas.

Este código é executado diretamente e fornece uma interface simples para a gestão de restaurantes em um ambiente de terminal.
"""

import os

restaurantes = []

def exibir_programa():
    print("""
    ██╗░░░██╗██╗░█████╗░███╗░░██╗░█████╗░░██████╗  ███████╗░█████╗░░█████╗░██████╗░
    ██║░░░██║██║██╔══██╗████╗░██║██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗
    ╚██╗░██╔╝██║███████║██╔██╗██║███████║╚█████╗░  █████╗░░██║░░██║██║░░██║██║░░██║
    ░╚████╔╝░██║██╔══██║██║╚████║██╔══██║░╚═══██╗  ██╔══╝░░██║░░██║██║░░██║██║░░██║
    ░░╚██╔╝░░██║██║░░██║██║░╚███║██║░░██║██████╔╝  ██║░░░░░╚█████╔╝╚█████╔╝██████╔╝
    ░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░
    """)

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastrar Restaurantes')

    while True:
        nome_restaurante = input("\nDigite o nome do restaurante (ou 'sair' para parar): ")
        
        if nome_restaurante.lower() == 'sair':
            menu()

        categoria_restaurante = input("Qual Categoria : ")
        ativo_restaurante = input("O restaurante está ativo? (s/n): ").lower() == 's'

        # Adiciona o restaurante à lista de restaurantes
        restaurantes.append({
            'Nome': nome_restaurante,
            'Categoria': categoria_restaurante,
            'Ativo': ativo_restaurante
        })

        print(f'O restaurante -- {nome_restaurante} -- foi cadastrado com sucesso!')

def listar_restaurante():
    os.system('cls')
    print('Listar Restaurantes\n')

    # Verifica se há restaurantes cadastrados
    if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado.\n")
    else:
        # Para cada restaurante na lista de restaurantes:
        for index, restaurante in enumerate(restaurantes):
            nome_restaurante = restaurante['Nome']
            categoria = restaurante['Categoria']
            ativo = "Ativo" if restaurante['Ativo'] else "Inativo"
            print(f'{index + 1}. {nome_restaurante} | {categoria} | {ativo}')

    input('\nPressione Enter para voltar ao menu.')
    menu()

def ativar_desativar_restaurante():
    os.system('cls')
    print('Ativar/Desativar Restaurantes\n')

    # Verifica se há restaurantes cadastrados
    if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado.\n")
    else:
        # Exibe a lista de restaurantes com o índice
        for index, restaurante in enumerate(restaurantes):
            nome_restaurante = restaurante['Nome']
            ativo = "Ativo" if restaurante['Ativo'] else "Inativo"
            print(f'{index + 1}. {nome_restaurante} | {ativo}')
        
        try:
            # Solicita o número do restaurante a ser alterado
            escolha = int(input("\nDigite o número do restaurante para alterar o status (ou 0 para voltar ao menu): "))
            
            if escolha == 0:
                menu()
            
            # Verifica se a escolha é válida
            if 1 <= escolha <= len(restaurantes):
                restaurante_selecionado = restaurantes[escolha - 1]

                # Alterna o status de ativo/inativo
                if restaurante_selecionado['Ativo']:
                    restaurante_selecionado['Ativo'] = False
                    print(f"\nO restaurante '{restaurante_selecionado['Nome']}' foi desativado.")
                else:
                    restaurante_selecionado['Ativo'] = True
                    print(f"\nO restaurante '{restaurante_selecionado['Nome']}' foi ativado.")
            else:
                print("Opção inválida, escolha um número válido.")
                ativar_desativar_restaurante()

        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            ativar_desativar_restaurante()
    
    input("\nPressione Enter para voltar ao menu.")
    menu()

def menu():
    while True:
        print('''
        1. Cadastrar Restaurantes
        2. Listar Restaurantes
        3. Ativar/Desativar Restaurantes
        4. Sair\n''')

        try:
            numero = int(input('Escolha uma opção: '))
            match numero:
                case 1:
                    cadastrar_restaurante()
                case 2:
                    listar_restaurante()
                case 3:
                    ativar_desativar_restaurante()
                case 4:
                    print('Ok, encerramos!')
                    quit()
                case _:
                    print('Opção Invalida, escolha um número que apresenta no menu!')
                    menu()
        except ValueError:
            print('Opção Invalida, escolha um número que apresenta no menu!')
            menu()

def main():
    exibir_programa()
    menu()

if __name__ == '__main__':
    main()
