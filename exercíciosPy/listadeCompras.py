#Em andamento....
print('========== Lista de Compras =========')
lista = []
inicia = 1
while (inicia == 1):
    item = str(input('Digite o nome de um item: '))
    qtd = int(input('Digite a quantidade para comprar: '))
    lista.append({item,qtd}) 
    inicia = int(input('Novo item? 1 - SIM ou 0 - NÃO: '))
   
print("Sua lista: {}".format(lista))

