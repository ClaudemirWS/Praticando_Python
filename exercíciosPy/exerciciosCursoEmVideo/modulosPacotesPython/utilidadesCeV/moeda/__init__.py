def dobro(valor):
    valor *= 2
    return moeda(valor)

def metade(valor):
    valor /= 2
    return moeda(valor)

def aumentar(valor, porc):
   valor += (valor*porc/100)
   str(valor)
   return moeda(valor)

def diminuir(valor, porc):
   valor -= (valor*porc/100)
   return moeda(valor)

def moeda(valor):
    valor =  str(f'R$ {valor:.2f}').replace('.',',')
    return valor

def resumo(valor, porcAum, porcRed):
    print('-' * 40)
    print(f"""O dobro de R$ {moeda(valor)} é {dobro(valor)}
A metade de {moeda(valor)} é {metade(valor)}
Um aumento de {porcAum}% é {aumentar(valor, porcAum)}
Uma redução de {porcRed}% é {diminuir(valor, porcRed)}""")
    print('-' * 40)