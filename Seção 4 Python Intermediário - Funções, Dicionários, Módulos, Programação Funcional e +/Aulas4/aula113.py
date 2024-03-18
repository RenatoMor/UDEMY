# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor da variável.


def multiplier(*args):  # '*args' Para receber quantos argumentos eu quizer
    total = 1
    for number in args:
        total *= number
    return total


multiplication = multiplier(1, 2, 3, 4, 5, 6)
print(multiplication)


# Crie uma função que fale se um número pe par ou impar, retorne se é par ou impar.
def pair_odd(numero):
    multiplo_de_dois =  numero % 2 == 0

    if numero % 2 == 0:
        return f'{numero} é par.'
    print(f'{numero} é impar.')


print(pair_odd(2))
print(pair_odd(3))
print(pair_odd(15))
print(pair_odd(20))







