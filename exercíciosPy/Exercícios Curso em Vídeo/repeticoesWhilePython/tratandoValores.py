print('========== TRATANDO VALORES ==========')
roda = True
quant = 0
soma = 0
while roda == True:    
    num = int(input('Digite um número ou digite 999 para sair: '))
    if (num != 999):
        quant += 1
        soma += num
    elif(num == 999):
        roda = False
        print('Saindo...')
if (soma > 0):
    print('A soma entre todos os {} números digitados é : {}'.format(quant,soma))
else: 
    print('Você não informou nenhum valor...')