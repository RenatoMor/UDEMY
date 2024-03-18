"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300 # Alterando o valor do índice 2
# del lista[2] # Apagando o valor do índice 2
# print(lista) # [10, 20, 40]
# print(lista[2]) # 40
lista.append(50) # Adicionando o valor 50 no final da lista
lista.pop() # Apagando o último valor da lista
lista.append(60) # Adicionando o valor 60 no final da lista
lista.append(70) # Adicionando o valor 70 no final da lista
ultimo_valor = lista.pop(3) # Apagando o valor do índice 3
print(lista, 'Removido,', ultimo_valor) # [10, 20, 30, 70] Removido, 40