n = input('Digite seu nome: ')
n = n.strip()
n1 = n.lower()
if 'silva' in n1:
    print(f'{n}, tem Silva em seu nome.')
else:
    print(f'{n}, não tem Silva em seu nome.')