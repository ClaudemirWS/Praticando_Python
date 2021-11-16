print('========== GOLS JOGADOR DE FUTEBOL ==========')
dcrn = {}
gol = []
dcrn['nome'] = str(input('Nome do jogador: ')).title().strip()
dcrn['partidas'] = int(input(f'Quantas partidas jogou o {dcrn["nome"]}: '))
if (dcrn['partidas'] != 0):
    for indice in range (1, dcrn['partidas']+1):
        dcrn['gols'] = gol.append(int(input(f'Gols na {indice}ª partida: ')))
        dcrn['total'] = sum(gol)
    print('========== RESUMO ==========')
    print(f"""O jogador {dcrn['nome']}, participou de {dcrn['partidas']} 
partidas e marcou um total de {dcrn['total']} gols.""")
    print('========== LISTA DE PARTIDAS ==========')
    for indice, gols in enumerate(gol):
        print(f'Na {indice+1}ª partida marcou {gols} gols.')
else:
    print(f'O jogador {dcrn["nome"]} não jogou nenhuma partida.')