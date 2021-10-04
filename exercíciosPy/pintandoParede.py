print('========= CÁLCULO DE TINTA NECESSÁRIA PARA PINTAR UMA PAREDE ==========')
lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = alt * lar
print('\nSua parede tem a dimensão de {}x{} e sua área equivale a {}m²\n'.format(lar,alt,area))
print('Para pintar essa parede, você precisará de {} litros de tinta!\n'.format(area/2))

