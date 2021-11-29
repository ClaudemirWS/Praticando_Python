inicia = True
op = 1
print('========== MENU DE OPÇÕES ==========')
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valoR: '))
while inicia == True:
    if (op == 1):
        menu = int(input("""    
    [ 1 ] Somar todos valores
    [ 2 ] Multiplicar todos valores
    [ 3 ] Mostrar maior valor
    [ 4 ] Trocar os dois valores
    [ 5 ] Sair do programa
    Escolha uma opção: """))    
    if (menu == 1):
        soma = v1+v2
        print('\n{} + {} = {}'.format(v1,v2,soma))
    elif (menu == 2):
        mult = v1*v2
        print('\n{} * {} = {}'.format(v1,v2,mult))
    elif (menu == 3):
        if (v1 > v2):
            maior = v1
            print('\n{} é o maior.'.format(maior))
        else:
            maior = v2
            print('\n{} é o maior.'.format(maior))
    elif (menu == 4):
        v1 = int(input('\nDigite o primeiro valor: '))
        v2 = int(input('Digite o segundo valoR: '))         
    elif (menu == 5):
        print('\nSaindo...')
        inicia = False
        exit()
    else:
        inicia = False
    op = int(input('\nDeseja ver o menu novamente? 1 - SIM ou 2 - Não: '))
    if (op == 2):
        print('\nSaindo...')
        inicia = False
        exit()