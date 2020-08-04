l = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro',34.9
print(50*'-')
print(f'\033[1m{"LISTAGEM DE PREÇO":^50}')
print(50*'-')
c = 0
for n in l:
    if c%2==0:
        print(f'{l[c]:.<41}',end='')
    if c%2==1:
        print(f'R${l[c]:>7.2f}')
    c+=1
print(50*'-')