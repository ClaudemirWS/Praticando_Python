print('========== BRASILEIRÃO 2021 ==========')
count = 0
countPlus = 17
time = ''
times = ('Atlético-MG','Palmeiras', 'Flamengo','Bragantino','Fortaleza','Corinthians',
'Internacional','Fluminense','América-MG','Cuiabá','Atlético-GO','São Paulo',
'Ceará','Athletico-PR','Santos','Bahia','Sport','Juventude','Grêmio','Chapecoense')

while True:
    op = int(input("""\nESCOLHA O QUE DESEJA VER: 
    [1] - TABELA BRASILEIRÃO
    [2] - CLASSIFICAÇÃO PARA LIBERTADORES
    [3] - ZONA DO REBAIXAMENTO 
    [4] - PESQUISAR TIME 
    [5] - SAIR DO PROGRAMA: """))

    #tabela completa
    if (op == 1):
        while True:
            count = 0
            print('\nTabela com os 20 times: ')
            while (count < 20):
                print(f'[{count+1}]', times[count])
                count += 1
            break

    #classificação para Libertadores
    elif (op == 2):
        while True:
            count = 0
            print('\nZona de classificação para Libertadores: ')
            while (count < 6):
                print(f'[{count+1}]', times[count])
                count += 1
            break

    #zona de rebaixamento
    elif (op == 3):
        while True:
            print('\nZona do Rebaixamento: ')
            for count in range (4):
                print(f'[{countPlus}]', times[count-4])
                countPlus+=1
            break

    #posição da chapecoense
    elif (op == 4):
        time = str(input('\nDigite o nome do time: ')).strip().title()
        print(f'O time {time} está na {times.index(time)+1}º posição.')

    else:
        print('\nSaindo...')
        break       

    #times em ordem alfabetica
    #print('\nOrdem alfabética: ', sorted(times),end=' ')