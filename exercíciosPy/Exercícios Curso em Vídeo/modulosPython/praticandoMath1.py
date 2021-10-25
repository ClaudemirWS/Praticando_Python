from math import trunc #aprendendo a importar modulos
print('========== MOSTRA PARTE INTEIRA DE UM NÚMERO REAL =========')
num = float(input('Digite um número real qualquer: '))
print('Você digitou {} e sua parte inteira é {}.'.format(num, trunc(num)))