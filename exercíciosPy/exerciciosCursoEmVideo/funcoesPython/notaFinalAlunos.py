print('========== MÉDIA DA TURMA ==========')
dcrn = {}
def notas(dados):
    status = ''
    maior = menor = media = 0
    for indice in dados:
        for notas in dados.values():
            if (indice == 'aluno1'):
                media += notas / len(dados)
                maior = menor = notas
            else: 
                if (maior <= notas):
                    maior = notas
                if (menor >= notas):
                    menor = notas
    if (media > 7):
        status = 'BOM'
    elif (media < 7):
        status = 'RUIM'
    elif (media >= 9):
        status = 'EXCELENTE'   
    print(f"""\nA maior nota foi {maior} e a menor nota foi {menor}, 
média geral da turma: {media:.2f}, situação da turma: {status}""")


#PROGRAMA PRINCIPAL
tam = int(input('Digite a quantidade de alunos: '))
for indice in range (1,tam+1):
    dcrn[f'aluno{indice}'] = float(input(f'Digite a nota do {indice}º aluno: '))
notas(dcrn)
