def leiaDinheiro(inp):
    while True:
        val = val2 = input(inp)
        cont = 0
        for c in val2:
            if c ==',' or c=='.':
                cont+=1
                val2 = val2.replace(c, '')
        if cont <= 1:
            if val2.isnumeric():
                val = val.replace(',', '.')
                val = float(val)
                break
            else:
                print(f'\033[1;31mERRO: "{val}" é um preço inválido!\033[m')
        else:
            print(f'\033[1;31mERRO: "{val}" é um preço inválido!\033[m')
    return val