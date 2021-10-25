print('========== Primeiro e último nome de uma pessoa ==========')
nome = str(input('Digite seu nome completo: ')).strip()
splitnome = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(splitnome[0].capitalize(),splitnome[-1].capitalize()))


