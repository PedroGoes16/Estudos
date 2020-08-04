try:
    n = int(input('Digite um número para consultar sua tabuada: '))
    print('============\n{} x  1 = {}\n{} x  2 = {}\n{} x  3 = {}\n{} x  4 = {}\n{} x  5 = {}\n{} x  6 = {}\n{} x  7 = {}\n{} x  8 = {}\n{} x  9 = {}\n{} x 10 = {}\n============'.format(n,n*1,n,n*2,n,n*3,n,n*4,n,n*5,n,n*6,n,n*7,n,n*8,n,n*9,n,n*10))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')
