print('========== PAR OU IMPAR ==========')
num = int(input('Digite um número: '))
resto = num % 2 #pega o resto da divisão por 2
if (resto == 0):
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))