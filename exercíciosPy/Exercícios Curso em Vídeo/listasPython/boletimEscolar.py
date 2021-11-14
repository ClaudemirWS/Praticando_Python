print('========== BOLETIM ==========')
lista = []
boletins = []
while True:
    nome = str(input("\nNome do aluno: ")).strip().title()
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digite a 2º nota: '))
    media = (nota1 + nota2) /2 
    lista.append([nome, [nota1, nota2], media])
    boletins.append(lista[:])
    lista.clear()
    continua = str(input('Deseja cadastrar novo aluno? S/N: ')).strip().upper()[0]
    if (continua == 'N'):
        print('Continuando...')
        break
print(f'\n{"Nº":<4}{"NOME":<10}{"MÉDIA":>10}')
for indice, varreLista in enumerate(boletins):
    for listar, alunos in enumerate(varreLista):
        print(f'{indice:<4}{alunos[0]:<10}{alunos[2]:>9}') #mostra na tela os dados
while True:
    roda = int(input('\nDigite o Nº de um aluno para ver suas notas (999 - SAIR): '))
    if (roda == 999):
        print('Saindo...')
        print('VOLTE SEMPRE.')
        break
    else:
        for indice, varreLista in enumerate(boletins):
            for listar, notas in enumerate(varreLista):
                if (indice == roda):
                    print(f'\nAs notas de {notas[0]} são : {notas[1]}')