import cadastraPessoa
def Menu():
    print('\n========== CADASTRO DE PESSOAS ==========')
    print("""
    1 - VER PESSOAS CADASTRADAS
    2 - CADASTRAR NOVA PESSOA
    3 - SAIR DO SISTEMA""")
    try:
        op = int(input('\nSua opção: '))
    except: 
        print('\n\033[31mOpção inválida! Tente novamente\033[m')
        Menu()
    else:
        #CADASTROS
        if (op == 1):
            cadastraPessoa.verCadastros()
        elif (op == 2):
            cadastraPessoa.cadastro()
        elif (op == 3):
            print('\n\033[32mFECHANDO PROGRAMA, Obrigado!\033[m')
            exit()
        else:
            print('\n\033[31mOpção inválida! Tente novamente\033[m')
            Menu()



