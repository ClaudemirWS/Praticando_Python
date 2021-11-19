print('========== SITUACÃO DO ELEITOR ==========')
def voto(id):
    """
    <--- CALCULA IDADE E NECESSIDADE DE VOTO DO ELEITOR --->
    id - recebe a idade atraves da funcao
    return - retorna a idade na posicao [0] e a situacao na posicao [1].
    <--- SITUACOES: OBRIGATORIO, NAO PERMITIDO E OPICIONAL --->
    """
    from datetime import date
    id = date.today().year - nasc 
    if (id > 18):
        sit = 'OBRIGATÓRIO'
    elif (id < 16):
        sit = 'NÃO PERMITIDO'
    elif (id >= 16 and id < 18 or id > 70):
        sit = 'OPICIONAL'
    return id, sit
#INCIO DO PROGRAMA  
nasc = int(input('Digite seu ano de nascimento: '))
print(f'Você tem {voto(nasc)[0]} anos de idade e seu voto é {voto(nasc)[1]}.')
help(voto)