try:
    a1 = float(input('Primeira nota de um aluno: '))
    a2 = float(input('Segunda nota desse aluno: '))
    m = (a1+a2)/2
    print('A média entre {} e {} é igual a {:.1f}.'.format(a1,a2,m))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')
