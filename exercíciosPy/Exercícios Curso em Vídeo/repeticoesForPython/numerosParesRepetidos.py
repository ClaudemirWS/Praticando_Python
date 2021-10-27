print('========== REPETIÇÃO DE NÚMEROS PARES ==========')
max = int(input('Deseja ver os pares até qual número? '))
for num in range (1,max):
    num = num + 1
    if (num % 2 == 0):
        print(num , end=' ') #se o número for par, repita sem pular linha