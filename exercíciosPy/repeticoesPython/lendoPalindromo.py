print('========== PALÍNDROMO ==========')
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
frase = frase.replace(' ', '') #remove espaços e deixa maiusculo
fraseinv = ''
for count in range (len(frase) -1, -1, -1): #inverte string a string   
    fraseinv = fraseinv + frase[count] #soma string a string ao inverso 
print('Digitado: {} / Inverso: {}'.format(frase, fraseinv)) #exibe inverso 
if (frase == fraseinv):
    print('É um PALÍNDROMO!')
else: 
    print('Não é um PALÍNDROMO!')


