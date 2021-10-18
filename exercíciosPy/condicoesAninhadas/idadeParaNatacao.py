from datetime import date
print('========== CLASSIFICAÇÃO DE IDADE PARA NATAÇÃO ==========')
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if (idade <= 9):
    classif = 'MIRIM'
elif (idade > 9 and idade <= 14):
    classif = 'INFANTIL'
elif (idade > 14 and idade <= 19):
    classif = 'JÚNIOR'
elif (idade > 19 and idade <= 25):
    classif = 'SÊNIOR'
elif (idade > 25):
    classif = 'MASTER'
else:
    print('Informação incorreta.')

print('Você tem {} anos e está classificado como {}.'.format(idade,classif))