print('========== 10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA =========')
pt = float(input('Primeiro Termo: '))
raz = float(input('Digite a razão: '))

for i in range (1,11,1):
    print(' -> {:.0f}'.format(pt), end='')
    pt = pt + raz    
print(' -> FIM')