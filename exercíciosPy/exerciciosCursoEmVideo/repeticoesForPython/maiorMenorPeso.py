print('========== MAIOR E MENOR PESO ==========')
peso = 0
pesoanterior = 0
pesomaior = 0
pesomenor = 0
for count in range (1,6):
    pessoa = float(input('Pessoa {}, PESO: '.format(count)))
    peso = pessoa
    if (pessoa > pesoanterior):
        pesomaior = pessoa
    elif(pessoa < pesoanterior):
        pesomenor = pessoa
    pesoanterior = peso
 
print('O maior peso foi {} / O menor peso foi {}'.format(pesomaior,pesomenor))



    
    



    