from typing import cast
import menuPrincipal
pessoasCad = []
def cadastro():
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()[0]
    pessoasCad.append([nome,idade,sexo])
    return pessoasCad, menuPrincipal.Menu()
def verCadastros():
    print(pessoasCad)
    return menuPrincipal.Menu()
    