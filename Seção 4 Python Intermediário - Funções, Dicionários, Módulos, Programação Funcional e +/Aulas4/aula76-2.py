# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Renato',
    'sobrenome': 'Moreira',
    'idade': 50,
}
print(pessoa.get('nome', 'Não existe'))


pessoa.setdefault('idade', '')
print(pessoa['idade'])
print(len(pessoa))  # Retorna a quantidade de chaves
print(list(pessoa.keys()))  # Retorna as chaves
print(tuple(pessoa.keys()))  # Retorna as chaves
print(list(pessoa.values()))
print(list(pessoa.items()))  # Retorna as chaves e o valor
print(list(pessoa.items()))  # Retorna as chaves e o valor

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)
# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)
# pessoa.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })

# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
pessoa.update(lista)
print(pessoa)