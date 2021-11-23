print('========== Analisando letras em frase ==========')
frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A letra A aparece primeiro na posição {}.'.format(frase.find('a')+1))#+1 serve para não iniciar em 0
print('A letra A aparece por último na posição {}.'.format(frase.rfind('a')+1))
