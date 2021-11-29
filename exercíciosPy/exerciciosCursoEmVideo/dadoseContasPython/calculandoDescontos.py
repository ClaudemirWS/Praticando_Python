print('========= APLICANDO DESCONTO DE 5% NO PRODUTO ==========')
prod = float(input('Digite o preço em R$ do produto: '))
porc = prod - (prod*5/100) #faz calculo em cima de 5%
print('\nO produto custava R${} e com o desconto equiavale a R${:.2f}'.format(prod,porc))


