print('========== Analisando Nome Completo =========')
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome completo em maiusculas: {}'.format(nome.upper()))
print('Seu nome completo em minusculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' '))) #subtrai a quantidade de espaços
nome = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nome[0], len(nome[0])))


