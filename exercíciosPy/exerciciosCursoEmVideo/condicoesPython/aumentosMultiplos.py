print('========== AUMENTOS MULTIPLOS DE SALÁRIO ==========')
salatual = float(input('Digite seu salário atual: R$'))
if (salatual <= 1250.00):    
    salaumento = salatual + (salatual * 15 / 100) #15% de aumento 
else:    
    salaumento = salatual + (salatual * 10 / 100) #10% de aumento
print('Seu novo salário será R$ {:.2f}'.format(salaumento))