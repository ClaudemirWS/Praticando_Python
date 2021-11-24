from utilidadesCeV import moeda, dado
print('========== EXERCITANDO MODULOS ==========')
num = dado.leiaDinheiro(print('Digite um valor: R$ ', end=''))
moeda.resumo(num, 25, 30)