print('========== DADOS DE UM JOGADOR ==========')
def ficha(jogador,marcados):
    if (jogador == ''):
        jogador = 'Desconhecido'
    if (marcados == ''):
        marcados = '0'
    return print(f'O jogador {jogador} fez {int(marcados)} gols.') 

#INICIO DO PROGRAMA
nome = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Gols marcados: '))
ficha(nome, gols)