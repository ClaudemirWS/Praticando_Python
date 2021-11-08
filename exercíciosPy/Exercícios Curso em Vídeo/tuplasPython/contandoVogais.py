print('========== CONTANDO VOGAIS ==========')
tupla = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO',
'PRATICAR','TRABALHAR','PROGRAMADOR','FUTURO','MERCADO')

for count in range (0, len(tupla)):
    print(f'\nNa palavra {tupla[count]} temos ', end='')
    for countVogais in tupla[count]:
        if countVogais in 'AEIOU':
            print(countVogais, end=' ')
        