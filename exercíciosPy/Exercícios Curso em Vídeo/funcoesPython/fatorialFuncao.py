print('========== FATORIAL USANDO FUNÇÕES ==========')
def fatorial(num, show=False):
    conta = num
    fat = 1
    while conta > 0: 
        if (show == True):   
            print('{}'.format(conta),end='')
            print(' x ' if conta > 1 else ' = ', end='' )
        fat = fat * conta
        conta -= 1    
    print(f'{fat}',end='') 

#INICIO DO PROGRAMA
num = int(input('Digite um número para ver seu fatorial: '))
mostra = int(input('1 - VER CÁLCULO COM RESULTADO / 2 - VER APENAS RESULTADO: '))
if (mostra == 1):
    fatorial(num,show=True)
elif (mostra == 2):
    fatorial(num,show=False)
else:
    fatorial(num,show=True)