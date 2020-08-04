try:
    p = float(input('Qual é o preço do produto? R$'))
    d = p*0.95
    print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(p,d))
except ValueError:
    print('Você inseriu um valor incoerente, tente novamente ;-)')
