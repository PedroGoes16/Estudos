print('\033[1;31;40m',10*'$','-','LOJAS PEDRO','-',10*'$','\033[m')
p = float(input('Qual o preço da compra? R$'))
f = int(input('0 -> dinheiro/cheque\n1 -> 1x no cartão\n2 -> 2x no cartão\n3 -> 3x ou mais no cartão\nForma de pagamento:  '))
if f == 0:
    p = p - 0.1*p
    print(f'O comprador pagará R${p:.2f} por essa compra, pois tem 10% de desconto.')
elif f == 1:
    p = p - 0.05*p
    print(f'O comprador pagará R${p:.2f} por essa compra, pois tem 5% de desconto.')
elif f == 2:
    print(f'O comprador pagará R${p:.2f} por essa compra em 2 parcelas de R${p/2:.2f} cada.')
elif f == 3:
    n = int(input('Insira o número de parcelas: '))
    p = p + 0.2*p
    print(f'O comprador pagará R${p:.2f} por essa compra em {n} parcelas de R${p/n:.2f} cada.\nLembrando que o aumento se deve aos 20% de juros do parcelamento!')
