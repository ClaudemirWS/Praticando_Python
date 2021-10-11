print('========== Listando Unidade, Dezena, Centena e Milhar =========')
num = str(input('Digite um número de 0 a 9999: '))
print('Você digitou {}, analisando..'.format(num))

if (len(num) == 1):
    print('Unidade: {}'.format(num[0]))    
elif (len(num) == 2):
    print('Unidade: {}'.format(num[1])) 
    print('Dezena: {}'.format(num[0])) 
elif (len(num) == 3):
    print('Unidade: {}'.format(num[2]))
    print('Dezena: {}'.format(num[1]))   
    print('Centena: {}'.format(num[0])) 
elif (len(num) == 4):
    print('Unidade: {}'.format(num[3]))
    print('Dezena: {}'.format(num[2])) 
    print('Centena: {}'.format(num[1])) 
    print('Milhar: {}'.format(num[0])) 
else: 
    print('Você não digitou um número de 0 a 9999!')





