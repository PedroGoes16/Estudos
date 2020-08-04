c = input('Digite o nome de uma cidade: ')
c = c.strip()
c1 = c.lower()
c1 = c1.split()
if c1[0] == 'santo':
    print(f'A cidade {c} começa com a palavra Santo.')
else:
    print(f'A cidade {c} não começa com a palavra Santo.')