print('========== STATUS DE UM ALUNO ==========')
dcrn = {}
dcrn['nome'] = str(input('Nome do(a) aluno(a): ')).strip().title()
dcrn['media'] = float(input(f'Media do(a) {dcrn["nome"]}: '))
if (dcrn['media'] >= 7):
    dcrn['status'] = 'Aprovado(a)'
elif (dcrn['media'] == 6):
    dcrn['status'] = 'Recuperação'
elif (dcrn['media'] <= 5):
    dcrn['status'] = 'Reprovado(a)'

print(f'O Aluno(a) {dcrn["nome"]} obteve média {dcrn["media"]} e está {dcrn["status"]}.')
