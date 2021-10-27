listaCandidatos = []
listavotos = []

print('===== ELEIÇÃO DO CONSELHO DE MORADORES DO BAIRRO =====')
comecaCadastro = int(input('\nComeçar a cadastrar candidatos? 1 - SIM ou 2 - NÃO: '))
    
if (comecaCadastro == 2):
    print('\nFinalizando...') 
    exit() 

while comecaCadastro == 1:#REGISTRA CANDIDATOS
    quantCandidados = int(input('Quantos candidatos deseja registrar? '))
    for count in range (1, quantCandidados+1):
        print('\n===== {}º REGISTRO ====='.format(count))
        pessoa = str(input('Nome do {}º candidato(a): '.format(count))).strip().title()  
        numPessoa = int(input('Número de votação do {}º candidato(a): '.format(count)))  
        listaCandidatos += [[numPessoa,pessoa]]
    comecaCadastro = 0

listarCandidatos = int(input('\nVer a lista de candidatos? 1 - SIM ou 2 - NÃO: '))

if (listarCandidatos == 1):#LISTAGEM DE CANDIDADOS
    print('\n===== LISTA DE CANDIDATOS =====')
    #organização de candidados
    for count in range (0,len(listaCandidatos)):
        if (count == 0):
            dadosCandidato = listaCandidatos[count]
            num = dadosCandidato[0] #vamos sempre usar 0 para número do candidato
            nome = dadosCandidato[1] #vamos sempre usar 1 para nome do candidato           
        else:                                        
            dadosCandidato = listaCandidatos[count]
            num = dadosCandidato[0] 
            nome = dadosCandidato[1]                  
        print('\nCandidato(a): {}, vote no nº {}.'.format(nome,num))
    listarCandidatos = 0

comecaVoto = int(input('\nComeçar votação? 1 - SIM ou 2 - NÃO: ')) 

if(comecaVoto == 1):#VOTAÇÃO
    print('\n===== VOTAÇÃO =====')
    while comecaVoto == 1: #roda o programa
        escolha = int(input('Digite o número do seu candidato: '))
        for count in range (0,len(listaCandidatos)):
            if (count == 0):
                dadosCandidato = listaCandidatos[count]
                num = dadosCandidato[0]
                nome = dadosCandidato[1]            
            else:                                        
                dadosCandidato = listaCandidatos[count]
                num = dadosCandidato[0]
                nome = dadosCandidato[1]        

            if (count == 0):
                if (escolha == num):
                    numVoto = num
                    votado = nome                    
            else: 
                if (escolha == num):
                    numVoto = num
                    votado = nome
        
        listavotos += [numVoto]#registra número de votos em uma listaCandidatos                                    
        
        if (numVoto != 0):    
            print('Você votou em {}, nº {}.'.format(votado,numVoto))                      
        else: 
            print('Você votou NULO.')

        numVoto = 0#zera o último votado

        comecaVoto = int(input('\nDeseja votar novamente? 1 - SIM ou 2 - NÃO: '))      

if (comecaVoto == 2):
    print('\nFinalizando...') 
    exit() 

comecaContagem = int(input('\nComeçar contagem de votos? 1 - SIM ou 2 - NÃO: '))

while comecaContagem == 1:#CONTAGEM DOS VOTOS
    print('\n===== RESULTADO DA ELEIÇÃO =====')
    for count in range (0,len(listaCandidatos)):
            if (count == 0):
                dadosCandidato = listaCandidatos[count]
                num = dadosCandidato[0]
                nome = dadosCandidato[1]  
                contagem = listavotos.count(num)                     
            else:                                        
                dadosCandidato = listaCandidatos[count]
                num = dadosCandidato[0]
                nome = dadosCandidato[1]
                contagem = listavotos.count(num)
            print('{}, nº {}, obteve {} votos.'.format(nome,num,contagem)) 
    comecaContagem = 0

else:#FINALIZA PROGRAMA
    print('\nFinalizando...') 
    exit()