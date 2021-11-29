print('========== LENDO INTEIROS ==========')
def leiaInt(n):
    print(n, end='')
    while True:
        n = str(input())
        if (n.isnumeric()):
            return int(n)
        else:
            print('Erro! Tente novamente: ', end='')
    
#PROGRAMA PRINCIPAL
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou {n}')