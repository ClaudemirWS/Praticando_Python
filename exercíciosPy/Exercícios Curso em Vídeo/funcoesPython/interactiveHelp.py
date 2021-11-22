print('========== INTERACTIVE HELP =========')
def Help():
    func = str(input('Nome da função: ')).strip().lower()
    while True:
        if (func != 'sair'):
            help(func)
        func = str(input('Digite outra função ou escreva SAIR: ')).strip().lower()
        if (func == 'sair'):
            print('FIM DO PROGRAMA')
            break

#INICIO DO PROGRAMA
Help()