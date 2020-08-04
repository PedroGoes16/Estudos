try:
    c = float(input('Informe a temperatura em °C: '))
    f = (9*c/5)+32
    print('A temperatura de {}°C corresponde a {:.1f}°F.'.format(c,f))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')