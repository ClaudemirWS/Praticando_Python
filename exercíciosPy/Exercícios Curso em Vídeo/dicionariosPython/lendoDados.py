print('========== DADOS DE PESSOAS ==========')
dcrn = {}
lista = []
quantPess = mediaIdades = 0
while True:
    dcrn['nome'] = str(input('Nome: ')).title().split()
    dcrn['sexo'] = str(input('Sexo M/F: ')).upper().split()[0]
    dcrn['idade'] = int(input('Idade: '))
    lista.append(dcrn.copy())
    lista.clear
    cont = int(input('Deseja cadastrar nova pessoa? 0 - NÃO ou 1 - SIM: '))
    if (cont == 0):
        print('Continuando...')
        break
for dados in lista:
    quantPess += 1
    mediaIdades += dados['idade']
print(f'\nA) Foram cadastradas {quantPess} pessoas.')
print(f'B) A média de idade entre todos é {(mediaIdades / quantPess):.2f}')     
print(f'C) Mulheres cadastradas: ', end=' ')
for dados in lista:
    if (dados['sexo'] == 'F'):
        print(dados['nome'], end=' ')   
print(f'\nD) Pessoas com idade maior que a média: ')
for dados in lista:
    if (dados['idade'] >= mediaIdades):
        print(f'     {dados["nome"]}, Sexo: {dados["sexo"]}, Idade: {dados["idade"]}')