from random import randint
print('========== NÚMEROS PARA A MEGA SENA ==========')
lista = []
jogos = []
vezes = int(input('Quantas vezes deseja sortear? '))
for indice in range (0, vezes):
    for sorteios in range (0, 6):
        num = randint(1,60)
        if (num not in lista):
            lista.append(num)
        elif (num in lista):
            num = randint(1,60)
            if (num not in lista):
                lista.append(num)
    jogos.append(lista[:])
    lista.clear()   
for indice, numeros in enumerate (jogos):
    print(f'O {indice+1}º sorteio foi: {numeros}',)
    