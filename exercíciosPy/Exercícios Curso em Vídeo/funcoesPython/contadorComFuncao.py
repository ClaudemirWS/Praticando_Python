print('========== CONTADOR ==========')
lista = []
def contador(inicio, final, passo):
    print('CONTANDO DE 1 ATÉ 10 DE 1 EM 1')
    for indice in range (0, 11, 1):
        lista.append(indice)
    for numeros in lista:
        print(numeros, end=' ')
    lista.clear()
    print()
    print('CONTANDO DE 10 ATÉ 1 DE 2 EM 2')
    for indice in range (0, 11, 2):
        lista.append(indice)
        lista.sort(reverse=True)
    for numeros in lista:
        print(numeros, end=' ')
    lista.clear()
    print()
    print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
    if (inicio and final > 0):
        for indice in range (inicio, final+1, passo):
            lista.append(indice)
        for numeros in lista:
            print(numeros, end=' ')
    elif (inicio < 0):
        for indice in range (inicio, final, passo):
            indice -= passo
            lista.append(indice)
        for numeros in lista:
            print(numeros, end=' ')
    elif (final < 0):
        for indice in range (inicio+1, final, 0 - (passo)):
            indice -= passo
            lista.append(indice)
        for numeros in lista:
            print(numeros, end=' ')
    lista.clear()
    return

#INICIO DO CÓDIGO
ini = int(input('Digite o inicio do contador: '))
fim = int(input('Digite o fim do contador: '))
pas = int(input('Digite o passo do contador: '))
contador(ini,fim,pas)
