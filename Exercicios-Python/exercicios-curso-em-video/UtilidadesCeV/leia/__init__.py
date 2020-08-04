def leia_int(i):
    while True:
        try:
            leit = int(input(i))
            break
        except ValueError:
            print('\033[1;31mERRO: por favor, digite um número inteiro válido!\033[m')
    return leit


def leia_float(i):
    while True:
        try:
            leit = float(input(i))
            break
        except ValueError:
            print('\033[1;31mERRO: por favor, digite um número real válido!\033[m')
    return leit
