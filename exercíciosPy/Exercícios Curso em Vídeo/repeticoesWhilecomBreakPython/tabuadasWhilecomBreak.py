print('========== TABUADAS ==========')
calc = count = 0
num = int(input('Digite um número ou digite 0 para sair: '))  
while True:      
    if (num != 0):        
        if (count < 10):
            count += 1 
            calc = num * count
            print(f'{num} x {count} = \033[31m{calc}\033[m') 
        elif (count == 10):
            count = 0
            num = int(input('Digite um número ou digite 0 para sair: '))    
    if (num == 0):
        break