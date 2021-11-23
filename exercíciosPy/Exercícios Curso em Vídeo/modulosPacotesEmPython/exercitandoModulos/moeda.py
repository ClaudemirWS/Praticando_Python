def dobro(valor):
    valor *= 2
    return valor

def metade(valor):
    valor /= 2
    return valor

def aumentar(valor):
   valor += (valor*10/100)
   str(valor)
   return valor

def diminuir(valor):
   valor -= (valor*10/100)
   return valor

def moeda(valor):
    valor =  str(f'R$ {valor:.2f}').replace('.',',')
    return valor
