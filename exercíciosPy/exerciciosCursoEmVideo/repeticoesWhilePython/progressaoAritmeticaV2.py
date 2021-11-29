
print('========== PROGRESSÃO ARITMÉTICA 2.0 ==========')
p1 = float(input('Digite o primeiro termo: '))
raz = float(input('Digite a razão: '))
roda = 0
max = 0
extra = 0
total = 0
#progressão aritmética usando While
print("===== TERMOS DE UMA P.A =====")
max = int(input('Quantos termos deseja ver: '))
while roda < max:#roda enquanto não atingir o limite pedido  
    total += 1      
    print('{:.0f} -> '.format(p1),end='')
    p1 = p1 + raz 
    roda += 1
    if (roda >= max):        
        print('Pausa')
        #variável que adiciona novo limite
        extra = int(input('\nMostrar mais termos? Digite 0 para sair: '))
        if (extra != 0):
            roda = 0
            max = extra            
        elif (extra == 0):
            print('Saindo...')            
print('Você viu {} termos de uma P.A'.format(total))            
print('FIM')