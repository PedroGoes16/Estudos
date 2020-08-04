s = float(input('Qual o sálario do funcionário? R$'))
if s > 1250:
    a = s + s*0.1
    print(f'O salário desse funcionário passará a ser R${a:.2f}, com um aumento de R${s*0.1:.2f}.')
else:
    a = s + s*0.15
    print(f'O salário desse funcionário passará a ser R${a:.2f}, com um aumento de R${s*0.15:.2f}.')