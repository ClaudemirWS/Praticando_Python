from random import randint
compJog = ''
soma = 0
print('===== PAR OU ÍMPAR =====')
print('Computador: Vou jogar PAR ou ÍMPAR com você!')
num = int(input('Escolha um número de 1 a 10: '))
while(True):
    comp = randint(1,10)
    soma += num + comp
    if (num <= 10):
        jog = str(input('Escolha P para PAR ou I para IMPAR: ')).strip().upper()   
        if (jog == 'P'):        
            compJog = 'I'
            print('Jogador Escolheu \033[34mPAR\033[m, computador vai de \033[32mÍMPAR\033[m.')
        elif (jog == 'I'):
            compJog = 'P'
            print('Jogador escolheu \033[32mÍMPAR\033[m, computador vai de \033[34mPAR\033[m.')
        if (soma % 2 == 0):
            if (jog == 'P'):
                print(f'{num} + {comp} = {soma}, \033[34mPAR!\033[m O jogador \033[36mVenceu!\033[m')
            else:
                print(f'{num} + {comp} = {soma}, \033[34mPAR!\033[m O jogador \033[31mPerdeu!\033[m')
        elif (soma % 2 != 0): 
            if (jog == 'I'):
                print(f'{num} + {comp} = {soma}, \033[32mÍMPAR!\033[m O jogador \033[36mVenceu!\033[m')
            else: 
                print(f'{num} + {comp} = {soma}, \033[32mÍMPAR!\033[m O jogador \033[31mPerdeu!\033[m')
    else:
        print('Escolha um número até 10!')
    break