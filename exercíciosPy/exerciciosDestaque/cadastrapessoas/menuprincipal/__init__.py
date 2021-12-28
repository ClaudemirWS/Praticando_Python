import cadastrapessoas
def menu():
    print('\n========== CADASTRO DE PESSOAS ==========')
    print("""
    1 - VER PESSOAS CADASTRADAS
    2 - CADASTRAR NOVA PESSOA
    3 - SAIR DO SISTEMA""")
    op = int(input('\nSua opção: '))
    # CADASTROS
    if (op == 1):
        cadastrapessoas.vercadastros()
    elif (op == 2):
        cadastrapessoas.cadastro()
    elif (op == 3):
        print('\n\033[32mFECHANDO PROGRAMA, Obrigado!\033[m')
        exit()
    else: 
        print('\n\033[31mOpção inválida! Tente novamente\033[m')
        op = int(input('\nSua opção: '))


