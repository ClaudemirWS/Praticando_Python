import menuprincipal
import titulosmenu
from time import sleep
pessoasCad = []

def cadastro():
    try:
        titulosmenu.mostratitulo('CADASTRO DE PESSOA')
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo M/F: ')).strip().upper()[0]
        pessoasCad.append([nome,idade,sexo])
        sleep(0.5)
        menuprincipal.menu()
        return pessoasCad
    except:
        print('\n\033[31mOpção inválida! Digite atentamente.\033[m')
        sleep(0.5)
        menuprincipal.menu()

def vercadastros():
    titulosmenu.mostratitulo('LISTA DE PESSOAS')
    if (len(pessoasCad) >= 1):
        for indice, pessoas in enumerate(pessoasCad):
            print(f'Pessoa {indice}: Nome: {pessoas[0]}, Idade: {pessoas[1]}, Sexo: {pessoas[2]}')
    else:
        print('\033[31m NENHUMA PESSOA CADASTRADA. \033[m')
    sleep(0.5)
    menuprincipal.menu()
    
    