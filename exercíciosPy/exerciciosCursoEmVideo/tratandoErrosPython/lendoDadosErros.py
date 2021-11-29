print('========== LENDO NÚMEROS ==========')
def leiaInt(num):
    print(num, end='')
    num = str(input()).strip()
    while True:
        try:
            return int(num)
        except:
            print(f'ERRO! Digite um número inteiro: ', end='')
            num = str(input())
def leiaFlt(num):
    print(num, end='')
    num = str(input()).strip()
    while True:
        try:
            return float(num)
        except:
            print(f'ERRO! Digite um número real: ', end='')
            num = str(input())
    
#PROGRAMA PRINCIPAL
numInt = leiaInt('Digite um número inteiro: ')
numFlt = leiaFlt('Digite um número real: ')
print(f'Você digitou o inteiro {numInt} e o real {numFlt}')
