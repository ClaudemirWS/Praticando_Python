print('========== PAR OU IMPAR V2 ==========')
lista = [[], []]
for count in range (1, 8):
    num = int(input(f'Digite o {count}º número: '))
    if (num % 2 == 0):
        lista[0].append(num)
    if (num % 2 == 1):
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"""Os números pares foram: {lista[0]}.
Os números ímpares foram: {lista[1]}.""")