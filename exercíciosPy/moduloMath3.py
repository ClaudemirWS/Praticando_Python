from math import sin,cos,tan,radians #aprendendo a importar modulos
print('========== SENO, COSSENO E TANGENTE =========')
ang = float(input('Digite um ângulo: ')) #recebe o ângulo
angrad = radians(ang) #converte o ângulo para radianos
print('O ângulo {} possui o SENO {:.2f}, o COSSENO {:.2f} e a TANGENTE {:.2f}.'.format(ang, sin(angrad), cos(angrad), tan(angrad)))