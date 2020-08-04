n = 0
s = []
while n!=999:
    n = int(input('Digite um número (caso queira sair digite: 999): '))
    s.append(n)
s.pop()
print(f'Você digitou {len(s)} números, são eles: {s}.\nE a soma entre eles é igual a {sum(s)}.')