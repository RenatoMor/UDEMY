import random

def gerar_cnpj():
    # Gera os 8 primeiros dígitos do CNPJ
    raiz_cnpj = f"{random.randint(10000000, 99999999):08d}"
    
    # Calcula os dois dígitos verificadores
    d1 = calcular_digito_verificador(raiz_cnpj)
    d2 = calcular_digito_verificador(raiz_cnpj + str(d1))
    
    # Retorna o CNPJ formatado
    return f"{raiz_cnpj[:2]}.{raiz_cnpj[2:5]}.{raiz_cnpj[5:8]}/0001-{d1:02d}{d2:02d}"

def calcular_digito_verificador(numero):
    # Implementação simples do cálculo de dígito verificador para CNPJ
    soma = 0
    peso = 2
    for digito in reversed(numero):
        soma += int(digito) * peso
        peso = peso + 1 if peso < 9 else 2
    
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

# Exemplo de uso
cnpj_gerado = gerar_cnpj()
print(cnpj_gerado)


# def gerar_numeros_formatados(ddd_inicial):
#     numeros_formatados = []
    
#     for _ in range(10):
#         ddd = ddd_inicial
#         numero = random.randint(100000000, 999999999)
#         numero_formatado = f"({ddd}) {numero // 10000}-{numero % 10000:04d}"
#         numeros_formatados.append(numero_formatado)
    
#     return numeros_formatados

# # Exemplo de uso com DDD inicial 21
# numeros_gerados = gerar_numeros_formatados(27)
# for numero in numeros_gerados:
#     print(numero)




# def gerar_numero_formatado():
#     ddd = random.randint(11, 99)  # Gera um DDD aleatório entre 11 e 99
#     numero = random.randint(100000000, 999999999)  # Gera um número de 9 dígitos aleatório
#     return f"({ddd}) {numero // 10000}-{numero % 10000:04d}"

# # Exemplo de uso
# numero_formatado = gerar_numero_formatado()
# print(numero_formatado)





# def gerar_numero_11_digitos():
#     # Gera um número aleatório com 10 dígitos e adiciona um dígito no início
#     numero_aleatorio = random.randint(10**9, 10**10 - 1)
#     return f"1{numero_aleatorio:010d}"  # Adiciona um "1" no início e formata para ter 11 dígitos

# # Exemplo de uso
# numero_gerado = gerar_numero_11_digitos()
# print(numero_gerado)
