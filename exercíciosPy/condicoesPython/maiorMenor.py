print('========== MENOR E MAIOR ==========')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#menor número
menor = n1
if (n2 < n1 and n2 < n3):
    menor = n2
if (n3 < n1 and n3 < n2):
    menor = n3
#maior número
maior = n1
if (n2 > n1 and n2 > n3):
    maior = n2
if (n3 > n1 and n3 > n2):
    maior = n3
print('O maior número foi {} e o menor número foi {}.'.format(maior,menor))