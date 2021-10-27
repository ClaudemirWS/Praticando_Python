from random import randint
num = randint(0,10)
jogadas = 1
print("""========= JOGO DE ADVINHAÇÃO ==========
Vou escolher um número de 0 a 10, tente advinhar!""")
print("\n===== VAMOS JOGAR =====")
jog = int(input('Em que número eu pensei? '))
while not jog  == num:
    if (jog > num):
        jog = int(input('Menos! Tente novamente!:  '))
    elif(jog < num):
        jog = int(input('Mais! Tente novamente!:  '))
    jogadas += 1
print('Acertou! Pensei no {}, você precisou de {} vezes para acertar.'.format(num,jogadas))