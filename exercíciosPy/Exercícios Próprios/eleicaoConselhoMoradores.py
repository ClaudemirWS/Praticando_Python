lista = []
cod = 0
inicia = 0
voto = 0
votado = ''

print('===== ELEIÇÃO DO CONSELHO DE MORADORES DO BAIRRO =====')
cand = int(input('Quantos candidatos deseja registrar? '))

for count in range (1, cand+1):#REGISTRA CANDIDATOS
    print('\n===== {}º REGISTRO ====='.format(count))
    pessoa = str(input('Registre o nome do {}º candidato: '.format(count))).strip().title()  
    cod = int(input('Registre o código de votação do {}º candidato: '.format(count)))    
    lista += [[cod,pessoa]]

ver = int(input('\nVer a lista de candidatos? 1 - SIM ou 2 - NÃO: '))
if (ver == 1):#LISTAGEM DE CANDIDADOS
    print('\n===== LISTA DE CANDIDATOS =====')
    #organização de candidados
    for count in range (0,len(lista)):
        if (count == 0):
            candidato = lista[count]
            num = candidato[0]
            nome = candidato[1]            
        else:                                        
            candidato = lista[count]
            num = candidato[0] 
            nome = candidato[1]                  
        print('\nCandidato: {}, vote no nº {}.'.format(nome,num))
    ver = 2

if(ver == 2):#INICIAR VOTAÇÃO?
    inicia = int(input('\nIniciar votação? 1 - SIM ou 2 - NÃO: ')) 

if(inicia == 1):#VOTAÇÃO
    print('\n===== VOTAÇÃO =====')
    escolha = int(input('Digite o número do seu candidato: '))
    for count in range (0,len(lista)):
        if (count == 0):
            candidato = lista[count]
            num = candidato[0]
            nome = candidato[1]            
        else:                                        
            candidato = lista[count]
            num = candidato[0]
            nome = candidato[1]        

        if (count == 0):
            if (escolha == num):
                voto = num
                votado = nome
        else: 
            if (escolha == num):
                voto = num
                votado = nome   
                    
    if (voto != 0):    
        print('Você votou em {}, nº {}.'.format(votado,voto)) 
    else: 
        print('Você votou NULO.')
          
elif(inicia == 2):#FINALIZA PROGRAMA CASO DESEJE NÃO VOTAR 
    print('\nFinalizando...') 
    exit()

else:#FINALIZA PROGRAMA
    print('\nFinalizando...') 
    exit()