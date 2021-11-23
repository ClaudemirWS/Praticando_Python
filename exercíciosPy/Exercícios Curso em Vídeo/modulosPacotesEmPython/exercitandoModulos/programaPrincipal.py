import moeda
print('========== EXERCITANDO MODULOS ==========')
num = float(input('Digite um valor: R$ '))
print(f"""O dobro de R$ {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}
A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}
Um aumento de 10% é {moeda.moeda(moeda.aumentar(num))}
Uma redução de 10% é {moeda.moeda(moeda.diminuir(num))}""")
