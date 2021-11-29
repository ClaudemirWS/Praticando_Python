print('========== MAIOR, MENOR E MÉDIA DE VÁRIOS VALORES ==========')
roda = True
soma = media = maior = menor = numAnt = 0
while roda == True:    
    num = int(input('Digite um valor qualquer ou digite 0 para sair: '))
    if (num != 0):  
        soma += num
        if (num > numAnt):        
            maior = num
        if (num < numAnt):        
            menor = num   
    elif (num == 0):        
        roda = False
        print('Saindo...') 
    else: #verifica novamente o maior e menor
        if (num > numAnt):        
            maior = num
        if (num < numAnt):        
            menor = num       
    numAnt = num       
media = soma / 2
print('A média entre os valores é {}'.format(media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior,menor))