print('========== LISTA DE PREÇOS ==========')
tupla = (
'Lápis',1.75,
'Borracha',2.00,
'Caderno',15.90,
'Estojo',25.00,
'Transferidor',4.20,
'Compasso',9.99,
'Mochila',120.32,
'Canetas',22.30 )

for count in range (0,len(tupla)):
    if (count % 2 == 0):
        print(f'{tupla[count]:.<28}', end='')
    elif (count % 2 == 1):
        print(f'R$ {tupla[count]:.2f}')


