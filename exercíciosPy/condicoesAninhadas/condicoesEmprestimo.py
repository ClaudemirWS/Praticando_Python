print('========== EMPRÉSTIMO PARA COMPRA DE CASA ==========')
print('O VALOR DA PRESTAÇÃO NÃO DEVE EXCEDER 30 POR CENTO DO SEU SALÁRIO.\n')
casaval = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário atual? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
#pega 30 por cento do salário
porcsal = sal*30/100
#pega valor da prestação em anos, dividido por 12 meses
prest = (casaval/anos)/12
#se a prestação superar 30% do salário o emprestimo é negado
print('\nA prestação será de \033[31mR${:.2f}\033[m'.format(prest))
if (porcsal < prest):
    print('30 por cento do seu salário equivale a R${:.2f},\033[31mEMPRÉSTIMO NEGADO!\033[m'.format(salporc))
elif (porcsal > prest):
    print('30 por cento do seu salário equivale a R${:.2f}, \033[32mEMPRESTIMO CONCEDIDO!\033[m'.format(salporc))
else:
    print('OPÇÃO DESCONHECIDA, ENCERANDO...')
    exit()



