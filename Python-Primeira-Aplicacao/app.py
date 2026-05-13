import os

restaurantes = ['Restaurante A', 'Restaurante B', 'Restaurante C']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

# Menu Principal
def voltar_ao_menu_principal():
    input('Pressione Enter para voltar ao menu principal...')
    main()

# Subtitulo
def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(f'--- {subtitulo} ---\n')
    print()

# Opção 1: Cadastrar restaurante
def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

# Opção 2: Listar restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    print('Restaurantes cadastrados:')
    for restaurante in restaurantes:
        print(restaurante)
    print()
    voltar_ao_menu_principal()

# Opção 3: Ativar restaurante
def ativar_restaurante():
    exibir_subtitulo('Ativar restaurante')
    pass

# Opção 4: Sair
def sair():
    finalizar_app()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o programa')
    print('Obrigado por usar o programa! Até a próxima!')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            ativar_restaurante()
        elif opcao_escolhida == 4: 
            sair()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()