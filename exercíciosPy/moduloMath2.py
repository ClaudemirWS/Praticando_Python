from math import hypot #aprendendo a importar modulos
print('========== COMPRIMENTO DA HIPOTENUSA =========')
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa é {:.2f}'.format(hypot(cato,cata)))