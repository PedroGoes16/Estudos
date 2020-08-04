try:
    m = float(input('Insira um valor em metro (m): '))
    k = m/1000
    h = m/100
    d = m/10
    dc = int(m*10)
    c = int(m*10**2)
    ml = int(m*10**3)
    print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m,k,h,d,dc,c,ml))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')
