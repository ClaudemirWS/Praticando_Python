import moeda
print('========== EXERCITANDO MODULOS ==========')
num = float(input('Digite um valor: R$ '))
print(f"""O dobro de R$ {num} é R$ {moeda.dobro(num)}
A metade de R$ {num} é R$ {moeda.metade(num)}
Um aumento de 10% em R$ {num} é R$ {moeda.aumentar(num)}
Uma redução de 10% em R$ {num} é R$ {moeda.diminuir(num)}""")
