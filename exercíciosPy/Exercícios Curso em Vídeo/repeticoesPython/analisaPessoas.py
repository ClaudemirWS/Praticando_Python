print('========== ANALISA DADOS DE PESSOAS ==========')
mediaIdade = 0
maiorIdade = 0
maisVelho = ''
maisJovens = 0
for count in range (1,5):
    print('===== {} Pessoa ====='.format(count))
    nome = str(input('Qual é o seu nome?: ')).strip()
    idade = int(input('Qual é a sua idade?: '))
    sexo = str(input('Qual é o seu sexo? M/F: ')).upper().strip()
    mediaIdade = mediaIdade + idade
    if (count == 1 and sexo == 'M'):
        maiorIdade = idade
        maisVelho = nome
    if (maiorIdade < idade and sexo == 'M'):
        maiorIdade = idade
        maisVelho = nome
    if (sexo ==  'F' and idade < 20):
        maisJovens = maisJovens + 1        
print('\nA media de idade entre todos é {} anos.'.format(mediaIdade/2))
print('O homem mais velho se chama {} e tem {} anos.'.format(maisVelho,maiorIdade))
print('O grupo tem {} mulheres com menos de 20 anos de idade.'.format(maisJovens))
