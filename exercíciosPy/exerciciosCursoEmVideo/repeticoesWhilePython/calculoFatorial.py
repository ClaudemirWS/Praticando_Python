print('========== FATORIAL ==========')
num = int(input('Digite um número para ver seu fatorial: '))
conta = num
fat = 1
while conta > 0:    
    print('{}'.format(conta),end='')
    print(' x ' if conta > 1 else ' = ', end='' )
    fat = fat * conta
    conta -= 1    
print('{}'.format(fat),end='')     
    
    
    