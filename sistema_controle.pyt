funcio_auto = set()
visit_auto = set()

while True:
    print('-'*15,'CONTROLE DE ENTRADA','-'*15)
    print('1 - Adicionar funcionario autorizado')
    print('2 - Adicionar visitante autorizado')
    print('3 - Verificar acessos')
    print('4 - Remover autorização')
    print('5 - Sair do sistema')
    print('-'*50)

    opcao = int(input("Digite qual opção deseja? :"))

    if opcao == 1:
        for i in range(2):
            nome = input('Insira o nome do funcionario para liberação : ')
            funcio_auto.add(nome)
            print(f'Acesso liberado para: {funcio_auto}')
            
            sair = input('Voltar ao menu? [s]im ou [n]ão: ').lower().startswith('s')
            if sair is True:
                break

            elif sair is False:
                continue        
    
    if opcao == 2:
        for i in range(2):
            nome = input('Insira o nome do visitante : ')
            visit_auto.add(nome)
            print(visit_auto)
            print(f'Acesso liberado para: {visit_auto}')
            
            sair = input('Voltar ao menu? [s]im ou [n]ão: ').lower().startswith('s')
            if sair is True:
                break

            elif sair is False:
                continue      
                
    if opcao == 3:
            print('ACESSOS PERMITIDOS')
            print(visit_auto)  
            print(funcio_auto)
            
            sair = input('Voltar ao menu? [s]im ou [n]ão: ')
            if sair is True:
                break

            elif sair is False:
                continue      
            
        
    if opcao == 4:
            nome = input('Digite o nome para remover: ')
            if nome in funcio_auto:
             funcio_auto.remove(nome)
            print(f"{nome} foi removido da lista de funcionários autorizados.")
                
    elif nome in visit_auto:
            visit_auto.remove(nome)
            print(f"{nome} foi removido da lista de visitantes autorizados.")
    else:
            print(f"{nome} não foi encontrado na lista de funcionários ou visitantes autorizados.")
            
    sair = input('Voltar ao menu? [s]im ou [n]ão: ').lower().startswith('s')
    if sair is True:
            break

    elif sair is False:
            continue    
            
    elif opcao == 5:
        sair = input('Deseja fechar o programa? [s]im ou [n]ão: ').lower().startswith('s')
    if sair is True:
        break
    elif sair is False:
        continue            