print('========== SOMA DE INTEIROS PARES ==========')
soma = 0
for count in range (1,7):
    num = int(input('Digite o {} inteiro: '.format(count)))
    if (num % 2 == 0):
        soma = soma + num
print('A soma de todos os números pares é: {}'.format(soma))