from random import randint
print('=-='*17)
print('Vou pensar em um número de 0 a 5, tente advinhar!')
print('=-='*17)
num = randint(0,5)
jog = int(input('\nEm que número eu pensei? '))

if (jog == num):
    print('VOCÊ ACERTOU! Pensei no número {}.'.format(num))
else:
    print('VOCÊ ERROU! Pensei no número {}.'.format(num))