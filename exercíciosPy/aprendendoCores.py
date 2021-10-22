print('\033[0;31;40m ========== CORES NO TERMINAL ==========\033[m')
nome = str(input('Digite seu nome e sobrenome: '))
cores = {'limpa':'\033[m',
        'azul':'\033[34m', 
        'amarelo':'\033[33m', 
        'vermelho':'\033[31m'}
print('Olá, {}{}{}!!'.format(cores['vermelho'], nome, cores['limpa']))
