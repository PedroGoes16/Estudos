try:
    l = float(input('Largura da parede: '))
    a = float(input('Altura da parede: '))
    ar = l*a
    t = ar/2
    print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l de tinta.'.format(l,a,ar,t))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')
