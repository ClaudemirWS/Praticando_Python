print('========= DIFERENÇA NO FALOR FINAL DE UM PRODUTO ==========')
prec = float(input('Qual o preço do produto em R$? '))
parce = int(input('Em quantas parcelas deseja pagar? (Máximo: 3x)'))

inicia = int(input('Digite 1 para continuar ou 0 para encerrar: '))

while (inicia == 1):

    if (parce == 1 or parce == 0):
        avista = prec - (prec*5/100)    
        print('\nO valor final do produto a vista ficará R$ {:.2f} com 5%'' de desconto.'.format(avista))
    elif (parce == 2):
        aumen = prec + (prec*5/100)
        print('\nO valor final do produto parcelado em {}x ficará R$ {:.2f} com 5%'' de aumento no valor total.'.format(parce,aumen))
    elif (parce == 3):
        aumen = prec + (prec*10/100)
        print('\nO valor final do produto parcelado em {}x ficará R$ {:.2f} com 10%'' de aumento no valor total.'.format(parce,aumen))
    else:
        print('\nTente novamente..')

    inicia = int(input('Digite 1 para realizar nova consulta ou 0 para sair.'))



