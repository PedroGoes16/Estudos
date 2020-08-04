def metade(n, form = False):
    if form:
        return moeda(n/2)
    else:
        return n/2


def dobro(n, form=False):
    if form:
        return moeda(n*2)
    else:
        return n*2


def aumentar(n, a, form=False):
    if form:
        return moeda(n+n*a/100)
    else:
        return n+n*a/100


def diminuir(n, d, form=False):
    if form:
        return moeda(n-n*d/100)
    else:
        return n-n*d/100


def moeda(val):
    return f'R${val:.2f}'


def resumo(val, a, r):
    print(30*'-')
    print(f'{"RESUMO DO VALOR":^30}')
    print(30*'-')
    print(f'{"Preço analisado: ":<20}{moeda(val):<10}')
    print(f'{"Dobro do preço: ":<20}{dobro(val, True):<10}')
    print(f'{"Metade do preço: ":<20}{metade(val,True):<10}')
    print(f'{a:>2}%{" de aumento: ":<17}{aumentar(val, a, True):<10}')
    print(f'{r:>2}%{" de redução: ":<17}{diminuir(val, r, True):<10}')
    print(30*'-')