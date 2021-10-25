print('========== MÉDIA ESCOLAR ==========')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2
print('Sua média é {}'.format(media))
if (media >= 7):
    print('Você está \033[034mAPROVADO!\033[m')
elif (media > 5 and media < 6.9):
    print('Você está em \033[033mRECUPERAÇÃO!\033[m')
elif (media < 5):
    print('Você está \033[031mREPROVADO!\033[m')
else:
    print('Informação incorreta.')
