print('========= APLICANDO AUMENTO DE 15% NO SALÁRIO ==========')
sal = float(input('Digite o seu salário atual: '))
aum = sal + (sal*15/100) #faz calculo em cima de 15% e soma ao salário
print('\nO seu salário de R${:.2f} e com o aumento irá somar R${:.2f}'.format(sal,aum))


