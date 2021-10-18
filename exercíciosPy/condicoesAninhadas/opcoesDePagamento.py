print('========== EFETUAÇÃO DE COMPRA ==========')
valor = float(input('Digite o valor da compra: R$'))
pag = int(input("""
Escolha a forma de pagamento:
[1] à vista em dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Digite sua opção: """))
if (pag == 1 or pag == 2):
    if (pag == 1):
        tipo = 'à vista em dinheiro, com desconto de 15%'
        final = valor - (valor * 15/100) #aplica 15% de desconto
        vezes = 1 #quantidade de parcelas
        parcelas = final / vezes #parcelas
    elif (pag == 2):
        tipo = 'à vista no cartão, com desconto de 10%'
        final = valor - (valor * 10/100) #aplica 10% de desconto
        vezes = 1 #quantidade de parcelas
        parcelas = final / vezes #parcelas
    else:
        print('Opção incorreta!')
        exit()
    print('Você escolheu a forma de pagamento {}, o total da compra foi R${:.2f}'.format(tipo,final)) 
else:
    if (pag == 3):
        tipo = '2x no cartão, sem juros'
        final = valor #valor normal
        vezes = 2 #quantidade de parcelas
        parcelas = final / vezes #parcelas 
    elif (pag == 4):
        tipo = '3x ou mais no cartão, com juros de 20%'
        vezes = int(input('Digite a quantidade de parcelas: ')) 
        final = valor + (valor * 20/100)  #aplica juros de 20%  
        parcelas = final / vezes #parcelas
    else:
        print('Opção incorreta!')
        exit()
    print("""Você escolheu a forma de pagamento {}, o total da compra
foi R${:.2f} em {} parcelas no valor de R${:.2f}.""".format(tipo,final,vezes,parcelas))



