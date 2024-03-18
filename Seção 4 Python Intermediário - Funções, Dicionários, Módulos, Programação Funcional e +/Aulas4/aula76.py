# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "valor".
# Chaves podem ser consideradas como "índice" que vimos na lista e podem ser do tipo imutáveis
# Como: str, int, float, bool, tuple
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list.



p1 = {
    'nome': 'Renato',
    'sobrenome': 'Moreira',
    'idade': 50,
    'altura': 1.67,
    'peso': 105,
    'enderecos': [
        {'rua': 'Niemeyer', 'número': 375, 'bairro': 'Vila Santa Lucia', 'estado': 'São Paulo', 'estado': 'SP'},
        {'rua': 'Urumila', 'número': 43, 'bairro': 'Jadim Primavera', 'estado': 'São Paulo', 'estado': 'SP'},
    ]
}
print(p1['enderecos'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]
# p1.update(lista)
# print(p1)
