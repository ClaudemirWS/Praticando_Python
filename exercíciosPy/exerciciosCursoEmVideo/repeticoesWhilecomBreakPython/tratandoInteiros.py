print('========== TRATANDO INTEIROS ==========')
soma = quant = 0
while True:    
    num = int(input('\nDigite um número inteiro ou digite 0 para sair: '))      
    if (num != 0):
        quant += 1
        soma = soma + num #FLAG preciso entender isso #FLAG
    if (num == 0):
        break

print(f"""\nVocê digitou \033[34m{quant}\033[m números. 
A soma dos números é \033[31m{soma}\033[m.""") #utilizando F strings