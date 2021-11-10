print('========== EXPRESSÕES MATEMÁTICAS ==========')
lista = []
parAbre = parFecha = 0
lista.append(str(input('Digite uma expressão matemática: ')))
for index, varreLista in enumerate(lista):
    if ( '(' in varreLista):
        for index, parenteses in enumerate (varreLista):
            if (parenteses == '('):
                parAbre += 1
            if (parenteses == ')'):
                parFecha += 1

print(f"""\nSua expressão tem {parAbre} parentêses abrindo 
e {parFecha} parentêses fechando a expressão.""")
if (parAbre > parFecha or parFecha > parAbre):
    print('\nPortanto, sua expressão está errada.')
elif (parAbre == parFecha and parFecha == parAbre):
    print('\nPortanto sua expressão está correta.')

        

    
    
