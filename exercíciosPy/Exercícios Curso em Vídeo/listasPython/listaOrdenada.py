print('========== LISTA ORDENADA ==========')
lista = []
for contador in range (0,5):
    num = int(input('Digite um valor: '))
    if (contador == 0 or num > lista[-1]):
        lista.append(num)
    else: 
        indices = 0
        while indices < len(lista): #enquanto os indices forem menores que o tamanho da lista
            if (num <= lista[indices]): #se o número for menor ou igual a algum item da lista
                lista.insert(indices, num) #adiciona o número no lugar deste item
                break
        indices += 1 #vai subindo na lista
print(f'Sua lista: {lista}')