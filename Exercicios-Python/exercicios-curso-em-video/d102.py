def fatorial(n,show = False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show (opcional): mostra ou não o calculo
    :return: O valor do fatorial de um número n.
    """
    print(30*'-')
    f = 1
    for c in range(n,0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f*=c
    return f


print(fatorial(5,show=False))
help(fatorial)
