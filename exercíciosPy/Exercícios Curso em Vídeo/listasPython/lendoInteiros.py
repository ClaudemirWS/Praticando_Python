print('========== LENDO INTEIROS ==========')
def leiaInt(n):
    print(n, end='')
    while True:
        try:
            n = int(input())
            break
        except: ValueError
        print('ERRO! DIGITE UM VALOR INTEIRO!')
        print(n, end='')
    return n
    
#PROGRAMA PRINCIPAL
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou {n}')