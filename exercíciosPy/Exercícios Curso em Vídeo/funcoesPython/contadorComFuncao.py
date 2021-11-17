print('========== CONTADOR ==========')
def contador(inicio, final, passo):
    #CONTAGEM REGRESSIVA ATÉ 0
    if (inicio > final and final == 0 and passo > 0):
        print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
        for indice in range (inicio, (final)-passo, 0 - (passo)):
            print(indice, end=' ')
    #OBSOLETO? CONTAGEM COM POSITIVOS
    if (inicio > 0 and final > 0):
        print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
        for indice in range (inicio, (final)+1, passo):
            print(indice, end=' ')
    print()
    #CONTAGEM FINAL NEGATIVO
    if (final < 0):
        #DECRESCENTE COM PASSO POSITIVO
        if (passo > 0):
            print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
            for indice in range (inicio, (final)-1, 0 - (passo)):
                print(indice, end=' ')
    #DECRESCENTE COM PASSO NEGATIVO
    if (passo < 0):
        print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
        for indice in range (inicio, (final)-1, passo):
            print(indice, end=' ')
    #CONTAGEM NEGATIVOS
    if (inicio < 0 and final < 0):
        print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
        for indice in range (inicio, (final)-1, passo):
            print(indice, end=' ')
    #CONTAGEM REGRESSIVA NEGATIVA ATÉ 0
    if (final > inicio and inicio == 0):
        print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
        for indice in range (inicio, (final)-passo, 0 - (passo)):
            print(indice, end=' ')
    #CONTAGEM PROGRESSIVA DE NEGATIVO PARA POSITIVO
    if (inicio < final):
        print(f'CONTANDO DE {inicio} ATÉ {final} DE {passo} EM {passo}')
        for indice in range (inicio, (final)+1, passo):
            print(indice, end=' ')
    return

#INICIO DO CÓDIGO
ini = int(input('Digite o inicio do contador: '))
fim = int(input('Digite o fim do contador: '))
pas = int(input('Digite o passo do contador: '))
contador(ini,fim,pas)