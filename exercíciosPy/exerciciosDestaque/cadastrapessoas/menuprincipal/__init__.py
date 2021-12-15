import cadastrapessoas
def menu():
    print('\n========== CADASTRO DE PESSOAS ==========')
    print("""
    1 - VER PESSOAS CADASTRADAS
    2 - CADASTRAR NOVA PESSOA
    3 - SAIR DO SISTEMA""")
    try:
        op = int(input('\nSua opção: '))
    except:
        print('\n\033[31mOpção inválida! Tente novamente\033[m')
        menu()
    else:
    # CADASTROS
        if (op == 1):
            cadastrapessoas.vercadastros()
        elif (op == 2):
            cadastrapessoas.cadastro()
        else:
            print('\n\033[32mFECHANDO PROGRAMA, Obrigado!\033[m')
            exit()

