print('========== CALCULANDO CUSTO DE VIAGEM ==========')
dist = float(input('Informe a distância da viagem em KM: '))
if (dist <= 200):
    prec = dist * 0.50
    print('Sua viagem tem {}KM e seu preço é R${:.2f}'.format(dist,prec))
else:
    prec = dist * 0.45
    print('Sua viagem tem {}KM e seu preço é R${:.2f}'.format(dist,prec))
print('Obrigado por viajar conosco!')