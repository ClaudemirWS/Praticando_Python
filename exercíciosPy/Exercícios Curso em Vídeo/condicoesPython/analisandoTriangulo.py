print('========== ANALISAOR DE TRIÂNGULOS ==========')
print('Digite três segmentos para vermos a possibilidade de um TRIÂNGULO.\n')
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
#um segmento precisa ser menor do que a soma dos outros dois
if (s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2):
    print('{} com {} com {} PODEM formar um TRIÂNGULO.'.format(s1,s2,s3))
else:
    print('\n{} com {} com {} NÃO PODEM formar um TRIÂNGULO.'.format(s1,s2,s3))

