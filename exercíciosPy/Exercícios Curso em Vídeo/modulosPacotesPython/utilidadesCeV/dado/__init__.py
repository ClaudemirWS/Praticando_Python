def leiaDinheiro(valor):
    valor = str(input()).strip().replace(',','.')
    while True:
        if(valor.isalpha() or valor.strip() == ''):
            valor = str(input('ERRO! Digite um valor: R$ ')).strip().replace(',','.')
        else:
            return float(valor)
