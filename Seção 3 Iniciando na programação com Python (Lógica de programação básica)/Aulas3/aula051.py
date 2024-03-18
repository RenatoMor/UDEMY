"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes # desempacotamento
print(nome2) # Helena

nome1, *resto = ['Maria', 'Helena', 'Luiz'] # empacotamento
print(nome1, resto) # resto é uma lista

_, _, nome, *resto = ['Maria', 'Helena', 'Renato'] # _ ignora o valor
print(nome) # Renato