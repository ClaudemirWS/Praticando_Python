from datetime import date
print('========== ANO BISSEXTO ==========')
ano = int(input('Digite um ano(Digite 0 para ver o ano atual): '))
#pega o ano atual pelo computador
if ano == 0:
    ano = date.today().year
#o resto da divisão por 4 tem que ser 0; o resto da divisão por 100 não pode ser 0; o resto da divisão por 400 tem que ser 0.
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0): 
    print('O ano de {} É BISSEXTO!'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(ano))
