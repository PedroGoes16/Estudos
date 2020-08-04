def leiaInt(i):
    print(30*'=')
    while True:
        n = input(f'{i}')
        if n.isnumeric():
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
    return int(n)



n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')