print("========== Radar Eletrônico ==========")
vel = float(input('Digite a velocidade registrada em KM/H: '))
if (vel > 80):
    multa = (vel - 80) * 7 #7 reais por cada KM acima da velocidade
    print('Ultrapassou a velocidade permitida!')
    print('Multa emitida no valor de R${:.2f}.'.format(multa))
else:
    print('Velocidade normal.')