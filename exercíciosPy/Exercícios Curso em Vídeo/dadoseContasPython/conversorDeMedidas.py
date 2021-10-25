#Converte metros em medidas acima e abaixo
print('========== CONVERSOR DE METROS ==========\n')
m = float(input('Digite a medida que deseja converter: '))
print('{} METROS em QUILÔMETROS é: {}'.format(m, m/1000)) 
print('{} METROS em HECTÔMETROS é: {}'.format(m, m/100))
print(' {} METROS em DECÂMETROS é: {}'.format(m, m*10))
print('{} METROS em  CENTÍMETROS é: {}'.format(m, m *100))
print('{} METROS em MILÍMETROS é: {}'.format(m, m *1000))