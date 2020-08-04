s = c = ma = me = 0
q = 's'
while q in 'Ss':
    n = int(input('Digite um número: '))
    s +=n
    c +=1
    q = input('Quer continuar?[S/N] ').strip()[0]
    if c == 1:
        ma = me = n
    if ma < n:
        ma = n
    if me > n:
        me = n
    if q not in 'SsNn':
        q = input('Voce digitou uma resposta incoerente, que continuar?[S/N] ')
print(f'A média entre todos os valores corresponde a {s/c:.2f}.\nO maior valor digitado foi {ma} e o menor foi {me}.')
