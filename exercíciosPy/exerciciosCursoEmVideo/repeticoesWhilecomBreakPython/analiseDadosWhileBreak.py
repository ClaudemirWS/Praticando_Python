print('========== ANALISANDO DADOS DE PESSOAS ==========')
cont = contIdade = contHomem = contMulher = 0
cad = int(input('Deseja cadastrar nova pessoa? 1 - SIM ou 2 - NÃO: '))
while True: 
    if (cad == 1):
        cont += 1
        idade = int(input(f'Digite a idade da {cont}ª pessoa: '))
        sexo = str(input(f'Digite o sexo da {cont}ª pessoa [M ou F]: ')).strip().upper()
        if (idade > 18):
            contIdade += 1
        elif (sexo == 'M'):
            contHomem += 1
        elif (sexo == 'F' and idade < 20):
            contMulher += 1
    elif (cad == 2):
        print('Saindo...')
        break
    else:
        print('Informação incorreta, tente novamente.')
    cad = int(input('Deseja cadastrar nova pessoa? 1 - SIM ou 2 - NÃO: '))
print(f"""
{contIdade} pessoas tem mais de 18 anos; 
{contHomem} homens foram contabilizados;
{contMulher} têm menos de 20 anos.""")
