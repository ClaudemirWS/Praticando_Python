print('========== SATUS DE IMC ==========')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

if (imc < 18.5):
    status = 'ABAIXO DO PESO'
elif (imc > 18.5 and imc < 25):
    status = 'PESO IDÉAL'
elif (imc > 25 and imc <= 30):
    status = 'ACIMA DO PESO'
elif (imc > 30 and imc <= 40):
    status = 'OBESIDADE'
elif (imc > 40):
    status = 'OBESIDADE MÓRBIDA'
else:
    print('Não foi possível realiza a operação.')

print('Seu IMC é {:.2f} e você está em estado de {}'.format(imc,status))