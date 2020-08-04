print(20*'-')
print('   LOJA DO PEDRAO')
print(20*'-')
pt = c = pm = 0
while True:
    n = input('Nome do produto: ').strip().upper()
    p = int(input('Preço: R$'))
    pt+=p
    pm+=1
    if pm == 1 or p<b:
        b = p
        no = n
    if p > 1000:
        c+=1
    while True:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        print(40 * '-')
        if q in 'SN':
            break
    if q == 'N':
        break
print('========== FIM DO PROGRAMA ==========')
print(f'O total da compra foi R${pt:.2f}.\nTemos {c} produtos custando mais de R$1000,00.\nO produto mais barato foi {no} custando R${b:.2f}.')