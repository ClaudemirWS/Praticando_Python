import time
print('========== CONTAGEM REGRESSIVA ==========')
num = 10
for i in range (1,11):  #laço de repetição 
   print('Ano Novo em {}'.format(num))
   time.sleep(1) #reduz processamento em 1 segundo
   num = num - 1 #contagem regressiva
   if (num == 0):
       print('\033[031mFELIZ ANO NOVO!!\033[m')
