try:
    n = int(input('Digite um número: '))
    a = n-1
    s = n+1
    print('Analisando o valor {}, seu antecessor é {} e o sucessor {}.'.format(n,a,s))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')
