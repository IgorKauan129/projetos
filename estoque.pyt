
estoque = {}

while True:
    print('-'*15,'Sistema do Estoque','-'*15)
    print('1 - Adicionar produto')
    print('2 - Atualizar quantidade de um produto')
    print('3 - Remover produto')
    print('4 - Exibir lista')
    print('5 - Sair do sistema')
    print('-'*50)

    opcao = int(input("Digite qual opção deseja? :"))


    while True:
        if opcao == 1:
            
            for i in range(2):
                produto = input('Nome do produto: ')
                if produto in estoque:
                    quantidade = int(input('Quantidade: '))
                    estoque[produto] = quant 
                else:
                    quant = int(input('Quantidade: '))
                    estoque[produto] = quant 

                    print(estoque)

            sair = input('Voltar ao menu? [s]im ou [n]ão: ').lower().startswith('s')
            if sair is True:
                    break

            elif sair is False:
                continue
            
        elif opcao == 2:
            produto = input("Digite o nome do produto para atualizar a quantidade: ")
            if produto in estoque:
                    quantidade = int(input("Digite a nova quantidade: "))
                    estoque[produto] = quantidade
                    print("Quantidade atualizada.")
                    
            else:
                print('Não existe na lista')
                
                
            sair = input('Voltar ao menu? [s]im ou [n]ão: ').lower().startswith('s')
            if sair is True:
                break
            
            elif sair is False:
                continue
        elif  opcao == 3:
                produto = input("Digite o nome do produto a ser removido: ")
                estoque.pop(produto, None)
                print('Produto removido')
                
                sair = input('Voltar ao menu? [s]im ou [n]ão: ').lower().startswith('s')
                if sair is True:
                        break

                elif sair is False:
                    continue
        elif opcao == 4:
                print('Seu estoque: ')
                if estoque:
                    print(estoque)
                    
                
                sair = input('Voltar ao menu? [s]im ou [n]ão: ').lower().startswith('s')
                if sair is True:
                        break

                elif sair is False:
                    continue
                
                        
                else:
                    print('lista vazia')
                    
                    sair = input('Sair do programa? [s]im ou [n]ão: ').lower().startswith('s')
                    if sair is True:
                            break

                    elif sair is False:
                        continue    
                    
        elif opcao == 5:
            print('Saindo do sistema...')
            
        
                          
                    
                    
                