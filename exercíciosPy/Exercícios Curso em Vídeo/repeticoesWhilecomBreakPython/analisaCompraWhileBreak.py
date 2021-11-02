print('========== ESTATÍSTICA DE COMPRAS ==========')
num = total = maisMil = precoAnt = 0
maisBarato = ''
while True:  
    print('*'*44)
    inicia = int(input('Comprar um produto: 1 - SIM ou 2 - NÃO: '))  
    if (inicia == 1):
        num += 1
        prod = str(input(f'Qual o nome {num}º do produto: ')).strip().title()
        preco = float(input(f'Qual o preço do {num}º produto: R$'))
        if (preco < precoAnt):
            maisBarato = prod
        if (preco > 1000):
            maisMil += 1         
        precoAnt = preco
        total += preco 
    elif (inicia == 2):
        print('Parando registro..')
        break
    else:
        print('Informação incorreta')   
print(f'O total de sua compra foi R${total:.2f}.')
print(f'{maisMil} produtos custam mais de R$1000.')
print(f'O produto mais barato foi {maisBarato}.')
