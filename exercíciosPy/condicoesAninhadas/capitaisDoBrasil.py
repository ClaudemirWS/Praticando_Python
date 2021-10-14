print('\033[;32m ========= CAPITAIS DO NORDESTE DO BRASIL ========== \033[m')
est = str(input('Digite o nome de um \033[031m estado nordestino \033[m para saber sua capital: ')).strip().lower()

if (est == 'pernambuco'):
    cap = 'recife'    
elif (est == 'rio grande do norte'):
    cap = 'natal'
elif (est == 'alagoas'):
    cap = 'maceió'
elif (est == 'sergipe'):
    cap = 'aracaju'
elif (est == 'bahia'):
    cap = 'salvador'
elif (est == 'ceará' or est == 'ceara'):
    est = 'ceará'
    cap = 'fortaleza'
elif (est == 'maranhão' or est == 'maranhao'):
    est = 'maranhão'
    cap = 'são luís'
elif (est == 'paraíba' or est == 'paraiba'):
    est = 'paraíba'
    cap = 'joão pessoa'
elif (est == 'piauí' or est == 'piaui'):
    est = 'piauí'
    cap = 'teresina'
else: 
    print('\033[033m\n Não corresponde a um estado do nordeste! \033[m\n')
    exit()

print('\n A capital do estado \033[33m{}\033[m é \033[34m{}\033[m!\n'
.format(est.capitalize(), cap.capitalize()))