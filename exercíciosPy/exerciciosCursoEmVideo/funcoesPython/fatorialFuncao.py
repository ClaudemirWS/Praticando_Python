print('========== FATORIAL USANDO FUNÇÕES ==========')
def fatorial(num, show=False):
    fat = 1
    for indice in range (num, 0, -1):
        if (show == True):   
            print('{}'.format(indice),end='')
            print(' x ' if indice > 1 else ' = ', end='' )
        fat *= indice
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