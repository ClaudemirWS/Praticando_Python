print('========== GOLS JOGADOR DE FUTEBOL ==========')
dcrn = {}
gol = []
jogador = []
escalados = []
continua = 'S'
while continua == 'S':
    dcrn['nome'] = str(input('\nNome do jogador: ')).title().strip()
    dcrn['partidas'] = int(input(f'Quantas partidas jogou o {dcrn["nome"]}: '))
    if (dcrn['partidas'] != 0): #se ele jogou ao menos uma partida
        for indice in range (1, dcrn['partidas']+1):
            gol.append(int(input(f'Gols na {indice}ª partida: ')))
            dcrn['gols'] = gol[:]
            dcrn['total'] = sum(gol)
    elif (dcrn['partidas'] == 0): #se ele não jogou nenhuma partida
        dcrn['gols'] = 0
        dcrn['total'] = 0
    continua = str(input('Outro jogador? S/N: ')).upper().strip()[0]
    jogador.append(dcrn.copy()) #faz copia do dicionário
    escalados.append(jogador[:]) #copia os dados do jogador em outra lista
    jogador.clear() #elimina informações para reescrever
    gol.clear()  #elimina informações para reescrever
print('\n========== RESUMO ==========')
print(f'{"Cód":>5} {"Nome":>5} {"Gols":>10} {"Total":>11}')    
for indice, jogadores in enumerate(escalados):
    for dados in jogadores:
        print(f'{indice:>3} {str(dados["nome"]):>10} {str(dados["gols"]):>9} {str(dados["total"]):>5}')
print('\n========== LISTA DE PARTIDAS ==========')
while True:
    roda = int(input('\nDigite o Nº de um jogador para ver suas partidas (999 - SAIR): '))
    if (roda == 999):
        print('Saindo...')
        print('Até logo.')
        break
    else:
        somaPart = 1
        for indice, varreLista in enumerate(escalados):
            if (indice == roda):
                for indices, dados in enumerate(varreLista):
                    if (dados['gols'] != 0): #se tiver dados na lista gols
                        for cadaGol in dados['gols']: #para cada gol, printe a partida e a quantidade de gols
                            print(f'Na {somaPart}ª partida marcou {cadaGol} gols.')
                            somaPart+=1
                    else: 
                        print('Não jogou nenhuma partida.')