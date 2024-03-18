import os
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_de_compras = []

print('\nEscolha uma opção:') 

while True:
# Inserir um item na lista de compras------------------------------------------
    opcao = input('\n[i]inserir, [a]apagar, [l]listar, [s]sair: ')
    if opcao == 'i':
        os.system('cls') # Limpa a tela
        print('Monte sua lista de compras!')
        item = input('Informe o item: ')
        lista_de_compras.append(item) # Função append insere o item na lista

# Apagar um item da lista de compras-------------------------------------------
    elif opcao == 'a':
        os.system('cls') # Limpa a tela
        print('Escolha um item para apagar:')
        try:
            for indice, item in enumerate(lista_de_compras): # Enumerate retorna o indice e o item
                print(f'[{indice}] {item}')    
            item = int(input())
            del lista_de_compras[item] # Função del apaga o item da lista
        except ValueError:
            print('Valor inválido! Digite um número inteiro.')        
        except IndexError:
            print('Valor inválido! Certifique-se de escolher um número válido.')
        
# Listar itens da lista de compras---------------------------------------------
    elif opcao =='l':
        os.system('cls') 
        if len(lista_de_compras) == 0:
            print('Lista vazia!')
            
        print('\nLista de compras:')
        print('----------------')
        for indice, item in enumerate(lista_de_compras):
            print(f'{indice}. {item}')

    elif opcao == 's':
        break

    else:
        print('Opção inválida!')

