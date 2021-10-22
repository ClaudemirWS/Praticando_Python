print('========== CONVERSOR DE BASE NÚMERICA ==========')
tipo = int(input("""
\033[31m 1 \033[m para BINÁRIO 
\033[31m 2 \033[m para OCTAL
\033[31m 3 \033[m para HEXADECIMAL
Digite o tipo de conversão: """))
num = int(input('Digite um número para converter: '))
if   (tipo == 1):    
    print('O número {} em binário é {}'.format(num,bin(num)[2:]))
elif (tipo == 2):
    print('O número {} em octal é {}'.format(num,oct(num)[2:]))
elif (tipo == 3):
    print('O número {} em hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('Opção Incorreta')
