from random import randint
print('========== PEDRA, PAPEL E TESOURA ==========')
jogador = int(input("""
[1] Pedra
[2] Papel
[3] Tesoura
Escolha sua jogada: """))
lista = ['Pedra', 'Papel', 'Tesoura']
computador = lista[randint(0,2)]

if (jogador == 1):
    jogada = lista[0]
    if (computador == lista[0]):
        print('EMPATE!')
    elif (computador == lista[1]):
        print('PERDEU!')
    elif (computador == lista[2]):
        print('VENCEU!')
elif (jogador == 2):
    jogada = lista[1]
    if (computador == lista[0]):
        print('VENCEU!')
    elif (computador == lista[1]):
        print('EMPATE!')
    elif (computador == lista[2]):
        print('PERDEU!')
elif (jogador == 3):
    jogada = lista[2]
    if (computador == lista[0]):
        print('PERDEU!')
    elif (computador == lista[1]):
        print('VENCEU!')
    elif (computador == lista[2]):
        print('EMPATE!')
else:
    print('Jogada inválida!')
    exit()

print('Você jogou {} e o Computador jogou {}.'.format(jogada, computador))




