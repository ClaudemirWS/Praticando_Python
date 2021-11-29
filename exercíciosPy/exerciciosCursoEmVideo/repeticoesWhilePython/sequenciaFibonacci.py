print('========== SEQUÊNCIA DE FIBONACCI ==========')
max = int(input('Quantos termos você quer mostrar? '))
roda = 0
n1 = 1
n2 = 0
n3 = 0
print('{} -> {} -> '.format(n2,n1),end='')
while roda < max:     
    n3 = n1 + n2
    n1 = n2 
    n2 = n3     
    print('{} -> '.format(n3),end='')      
    roda += 1
print('FIM')
    
   