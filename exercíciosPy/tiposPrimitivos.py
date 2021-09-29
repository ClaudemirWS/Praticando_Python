#Verifica tipos primitivos e utiliza metodos "is"
print(' ===== Vamos dissecar uma variável! ===== ')

v = input('Digite algo: ')

print('O tipo primitivo desse valor é: {} '.format(type(v)))

print('Possui espaços? {} '.format(v.isspace()))

print('É numerico? ',v.isnumeric())

print('É alfabético? ',v.isalpha())

print('É alfanumerico? ',v.isalnum())

print('Está em minusculas? ',v.islower())

print('Está em maiusculas? ',v.isupper())

print('Está capitalizado? ',v.istitle())

print('O tipo primitivo desse valor é: {} '.format(type(v)))