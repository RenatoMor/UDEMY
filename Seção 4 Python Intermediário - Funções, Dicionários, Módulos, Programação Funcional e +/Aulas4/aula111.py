# *args

# args empacota o valor enviado para uma função numa tupla
# (*args) Desempacota uma tupla para enviar como parametros para a função.
def soma(*args):
    total = 0
    for num in args:
        total += num
        print('Resultado da soma', total)
        print('Soma', total, '+',  num)





soma(1, 2, 3, 4, 5, 6, 7, 8, 9)