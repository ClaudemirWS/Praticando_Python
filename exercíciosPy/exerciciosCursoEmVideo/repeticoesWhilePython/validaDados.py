print('========== VALIDA DADOS ==========')
gen = str(input('Digite o seu gênero, M ou F: ')).strip().upper()
while gen not in ('MF'):
    gen = str(input('Você digitou errado, escolha M ou F: ')).strip().upper()
print('Você escolheu {}'.format(gen))