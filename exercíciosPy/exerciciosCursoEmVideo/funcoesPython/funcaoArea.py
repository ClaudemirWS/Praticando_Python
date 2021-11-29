print('========== CALCULO DE ÁREA DE UM TERRENO ==========')
def areaCalc(lar, comp):
    area = lar * comp
    print(f'\nA área de um terreno {lar} x {comp} é de {area:.1f}m².')

num1 = float(input('Digite a largura do terreno (m): '))
num2 = float(input('Digite o comprimento do terreno (m): '))
areaCalc(num1,num2)



