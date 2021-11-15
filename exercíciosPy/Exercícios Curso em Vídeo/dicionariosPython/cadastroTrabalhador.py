from datetime import date
print('========== CADASTRO DE TRABALHADOR ==========')
dcrn = {}
dcrn['nome'] = str(input('Seu nome: '))
dcrn['nasc'] = int(input('Ano de nascimento: '))
dcrn['idade'] = date.today().year - dcrn['nasc'] 
dcrn['ctps'] = int(input('Carteira de Trabalho (0 - NÃO TEM): '))
if (dcrn['ctps'] != 0):
    dcrn['anocontr'] = int(input('Ano de contrataçao: '))
    dcrn['salar'] = float(input('Seu salário: R$ '))
    dcrn['inss'] = ((dcrn['anocontr'] + 35) - date.today().year) + dcrn['idade']
    print('\n========== INFORMAÇÕES ==========')
    print(f"""A pessoa {dcrn["nome"]}, de {dcrn["idade"]} anos,
nascido em {dcrn["nasc"]}, carteira profissional Nº {dcrn["ctps"]},
irá se aposentar aos {dcrn["inss"]} anos de idade.""")
else: 
    print('\n========== INFORMAÇÕES ==========')
    print(f"""A pessoa {dcrn["nome"]}, de {dcrn["idade"]} anos,
nascido em {dcrn["nasc"]}, não possui carteira assinada.""")
