print('\033[1;33;46m', 20*'$$', '\033[m')
print('\033[1;36;43m','         SONHO DA CASA PRÓPRIA          ','\033[m')
print('\033[1;33;46m', 20*'$$', '\033[m')
c = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o salário do comprador? R$'))
t = int(input('Em quantos  anos ele irá pagar? '))
a = s*0.3
p = c/(t*12)
if p>=a:
    print('A parcela excedeu 30% do salário do comprador!\nInfelizmente não podemos realizar o empréstimo!')
else:
    print(f'PARABÉNS!!!\nO empréstimo pode ser realizado!\nAs parcelas terão um valor de R${p:.2f}.\nDurante {t*12} meses.')