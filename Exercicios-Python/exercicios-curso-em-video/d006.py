try:
    n = int(input('Digite um número: '))
    d = 2*n
    t = 3*n
    r = n**0.5
    print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n,d,n,t,n,r))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')
