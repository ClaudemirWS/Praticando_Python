print('========== NÚMERO PRIMO ==========')
num = int(input('Digite um número inteiro: '))
div = 0
print('{} é divisível por: '.format(num), end='')
for cont in range (1,num+1,1): #+1 porque não exite divisão por 0  
    if (num % cont == 0): #se o resto da divisão for 0
        div = div + 1 #é divisivel
        print('{}'.format(cont), end=' -> ') #printa os divisíveis               
print('FIM')
if (div == 2): #se o número só é divisivel por 1 e ele mesmo, é primo
    print('O número {} é primo'.format(num))
else:    
    print('O número {} não é primo'.format(num))