from datetime import date
print('========== ALISTAMENTO MILITAR ==========')
nasc = int(input('Digite seu ano de nascimento: '))
userIdade = date.today().year - nasc

print('Você nasceu em {} e tem {} anos, é OBRIGATÓRIO SE ALISTAR aos 18 anos.'.format(nasc,userIdade))

if (userIdade > 18):
    print('Você está {} anos atrasado para o ALISTAMENTO.'.format(userIdade-18))
elif (userIdade < 18):
    print('Você AINDA NÃO PRECISA SE ALISTAR, faltam {} anos.'.format(18-userIdade))
elif (userIdade == 18):
    print('Você está na IDADE PARA ALISTAMENTO1 PARABÉNS!')
else:
    print('Ano de nascimento incorreto.')