print('========== CAIXA ELETRÔNICO ==========')
saque = ced50 = ced20 = ced10 = ced1 = 0
valor = int(input('Quanto deseja sacar: R$'))
while True:
    while (valor > 0):           
        if (valor >= 50):
            saque += 50
            valor -= 50
            ced50 += 1            
        elif (valor >= 20):
            saque += 20
            valor -= 20
            ced20 += 1
        elif (valor >= 10):
            saque += 10
            valor -= 10
            ced10 += 1
        elif (valor >= 1):
            saque += 1
            valor -= 1            
            ced1 += 1
    if (valor == 0):
        print(f'Você sacou R${saque}.')
        if (ced50 >= 1):
            print(f'Você recebeu {ced50} cédulas de R$50')
        if (ced20 >= 1):
            print(f'Você recebeu {ced20} cédulas de R$20')
        if (ced10 >= 1):
            print(f'Você recebeu {ced10} cédulas de R$10')
        if (ced1 >= 1):
            print(f'Você recebeu {ced1} cédulas de R$1')
        break
    else:
        print('Algo deu errado.')
        break