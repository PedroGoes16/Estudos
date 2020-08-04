try:
    d = int(input('Quantos dias alugado? '))
    k = int(input('Quantos Km rodados? '))
    p = 60*d + 0.15*k
    print('O total a pagar é de R${:.2f}.'.format(p))
except ValueError:
    print('Você inseriu um dado incoerente, tente novamente ;-)')