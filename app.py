import os

restaurantes = ['mileninha grills','pizza melenas']

def exibir_nome_do_programa():
    print('𝖒𝖊𝖗𝖊𝖓𝖉𝖎𝖓𝖍𝖆 ( ͡👁 ͜ʖ ͡👁)\n')

def exibir_opcoes():
    print('1- cadastrar restaurante')
    print('2- listar restaurantes')
    print('3- ativar restaurante')
    print('4- sair\n')

def sair_app():
    os.system('cls')
    print('saindo do app\n')

def opcao_invalida():
    print('opção invalida!\n')
    input('pressione enter para voltar ao inicio')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante) 
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('pressione enter para ir ao inicio')
    main()

def listar_restaurantes():
    os.system('cls')
    print('listagem de restaurantes\n')
    for restaurante in restaurantes:
        print(f'*{restaurante}')
    input('pressione enter para ir ao inicio')
    main()


def opcao_escolha():
    try:
        opcao_escolhida = int(input ('escolha uma opção:  '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()       
        elif opcao_escolhida == 3:
            print('ativar restaurante')       
        elif opcao_escolhida == 4:
            sair_app()      
        else:
            opcao_invalida()     
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    opcao_escolha()





if __name__ == '__main__':
    main() 