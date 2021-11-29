print('========== COMPARANDO NÚMEROS ==========')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if (num1 > num2):
    print('O número {} é maior que o número {}'.format(num1,num2))
elif (num2 > num1):
    print('O número {} é maior que o número {}'.format(num2,num1))
elif (num1 == num2 and num2 == num1):
    print('Os dois números são iguais!')
else:
    print('Opção incorreta!')