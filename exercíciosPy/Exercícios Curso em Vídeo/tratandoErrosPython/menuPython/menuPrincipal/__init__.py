import cadastraPessoa
def Menu():
    print('========== CADASTRO DE PESSOAS ==========')
    print("""
    1 - VER PESSOAS CADASTRADAS
    2 - CADASTRAR NOVA PESSOA
    3 - SAIR DO SISTEMA""")
    try:
        op = int(input('Sua opção: '))
    except: 
        op = int(input('Opção inválida, tente novamente: '))
    #CADASTROS
    if (op == 1):
        cadastraPessoa.verCadastros()
    elif (op == 2):
        cadastraPessoa.cadastro()
    elif (op == 3):
        print('Fechando programa, obrigado!')
        exit()


