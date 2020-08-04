m = 0
mv = ''
med = []
mu = []
for c in range(1,5):
    print(7*'-', f'{c}ª PESSOA', 7*'-')
    n = input('Nome: ').strip().lower()
    i = int(input('Idade: '))
    s = input('Sexo [M/F]: ').strip().lower()
    med.append(i)
    if s == 'm' and i > m:
        m = i
        mv = n
    if s == 'f' and i < 20:
        mu.append(n)
print(50*'=')
print(f'A média da idade do grupo é de {sum(med)/len(med):.1f} anos.')
print(f'O homem mais velho tem {m} anos e se chama {mv.title()}.')
mul = ', '.join(mu)
print(f'{len(mu)} mulher(es) tem menos de 20 anos, é(são) ela(s): {mul.title()}')