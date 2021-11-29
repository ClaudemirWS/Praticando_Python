print('========== Número por Extenso ==========')
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete',
'oito','nove','dez','onze','doze','treze','quatorze','quinze')
num = int(input('Digite um número de 0 a 15: '))
while True:
    if (num == 0 or num <= 15):
        print(f'Por extenso é {tupla[num]}.')
        break
    else:
        num = int(input('Tente de novo, um número de 0 a 14: '))