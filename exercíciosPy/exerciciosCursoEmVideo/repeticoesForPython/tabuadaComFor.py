print('========== TABUADA COM REPETIÇÃO ==========')
tab = int(input('Digite um número para ver sua tabuada: '))
num = 0
for i in range (0,10):
    num = num + 1     
    print('{} x {} = {}'.format( tab, num, tab*num))