print('========== PROGRESSÃO ARITMÉTICA 2.0 ==========')
p1 = float(input('Digite o primeiro termo: '))
raz = float(input('Digite a razão: '))
roda = 0
#progressão aritmética usando While
while roda < 10:
    print('{:.0f} -> '.format(p1),end='')
    p1 = p1 + raz
    roda += 1
print('FIM')
