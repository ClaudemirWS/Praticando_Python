print('Calculadora Simples\n')
inicia = 1

while inicia == 1:
    
    print('Escolha o tipo de operação que deseja fazer: \n+\n-\n*\n/\n')
    op = str(input())

    print('\nDigite o primeiro número que fará parte do cálculo')
    num1 = int(input())

    print('Digite o segundo número que será calculado')
    num2 = int(input())

    if (op == '+'): 
        print('\n {} + {} = {}'.format(num1,num2, num1 + num2))

    elif (op == '/'): 
        print('\n {} / {} = {}'.format(num1,num2, num1 / num2))

    elif (op == '*'): 
        print('\n {} * {} = {}'.format(num1,num2, num1 * num2))

    elif (op == '-'): 
        print('\n {} - {} = {}'.format(num1,num2, num1 - num2))
    else:
        print('Tipo de operação não definido\n')
        inicia = int(input('\nDeseja tentar novamente? (0 - NÃO / 1 - SIM): '))

    inicia = int(input('\nDeseja realizar novo cálculo: (0 - NÃO / 1 - SIM): '))
    

