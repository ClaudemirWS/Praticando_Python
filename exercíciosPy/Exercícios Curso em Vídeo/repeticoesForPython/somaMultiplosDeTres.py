print('========== SOMA DE 500 ÍMPARES MÚLTIPLOS DE TRÊS ==========')
soma = 0
quant = 0
for cont in range (1,501,2):
    if (cont % 2 == 1 and cont % 3 == 0):   
        soma = soma + cont
        quant = quant + 1           
        print(cont , end=' ') #se o número for ímpar, mostre sem pular linha 
print('\nA Soma de todos os {} números é {}'.format(quant, soma))       
