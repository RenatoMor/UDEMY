"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
# variavel = 'Olá mundo'
# print(variavel[::-1])

# Exemplo de fatiamento

saudacao = 'Bom dia, Boa tarde, Boa noite'

print(saudacao[0:7])
print()
print(saudacao[9:18])
print()
print(saudacao[20:29])
print()
print(saudacao[0:len(saudacao):1])


