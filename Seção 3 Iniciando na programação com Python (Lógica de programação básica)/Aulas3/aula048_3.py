"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40] # Lista de valores
lista.append('Renato') # Adiciona o valor 'Renato' no final da lista
nome = lista.pop() # Apaga o último valor da lista
lista.append(1233) # Adiciona o valor 1233 no final da lista
del lista[-1] # Apaga o último valor da lista
# lista.clear() # Apaga todos os valores da lista
lista.insert(100, 5) # Adiciona o valor 5 no índice 100
print(lista[4]) 