from math import trunc #aprendendo a importar modulos
print('========== MOSTRA PARTE INTEIRA DE UM NÚMERO REAL =========')
num = float(input('Digite um número real qualquer: '))
print('O que vem antes da virgula no número digitado é {}'.format(trunc(num)))