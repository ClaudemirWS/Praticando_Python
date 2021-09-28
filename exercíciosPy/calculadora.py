print('Calculadora Simples\n') #Titulo do programa
inicia = 1 #variavel para o do/while

while inicia == 1: #roda o programa
    
    print('Escolha o tipo de operação que deseja fazer: \n+\n-\n*\n/\n')
    op = str(input()) #coleta tipo de operação

    print('\nDigite o primeiro número que fará parte do cálculo')
    num1 = int(input()) #coleta primeiro operador

    print('Digite o segundo número que será calculado')
    num2 = int(input()) #coleta segundo operador

    #realiza operação baseado na escolha do usuário e faz o print
    if (op == '+'): 
        print('\n {} + {} = {}'.format(num1,num2, num1 + num2))

    elif (op == '/'): 
        print('\n {} / {} = {}'.format(num1,num2, num1 / num2))

    elif (op == '*'): 
        print('\n {} * {} = {}'.format(num1,num2, num1 * num2))

    elif (op == '-'): 
        print('\n {} - {} = {}'.format(num1,num2, num1 - num2))
    else:
        #opção caso usuario erre tipo de operação
        print('Tipo de operação não definido\n')
        inicia = int(input('\nDeseja tentar novamente? (0 - NÃO / 1 - SIM): '))

    #opção de rodar o programa novamente
    inicia = int(input('\nDeseja realizar novo cálculo: (0 - NÃO / 1 - SIM): '))
    

