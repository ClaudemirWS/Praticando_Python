print('========== ANALISAOR DE TRIÂNGULOS ==========')
print('Digite três segmentos para vermos a possibilidade de um TRIÂNGULO.\n')
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
#um segmento precisa ser menor do que a soma dos outros dois
if (s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2):
    if (s1 == s2 and s1 == s3 and s2 == s3):
        tipo = 'EQUILÁTERO'
    elif (s1 == s2 or s1 == s3 or s2 == s3):
        tipo = 'ISÓSCELES'
    elif (s1 != s2 and s1 != s3 and s2 != s3): 
        tipo = 'ESCALENO'
    print('Os seguimentos PODEM formar um TRIÂNGULO {}.'.format(tipo))
else:
    print('\nOs seguimentos NÃO PODEM formar um TRIÂNGULO.')