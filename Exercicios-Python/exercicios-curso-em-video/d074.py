from random import randint
s = randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)
print('Os valores sorteados foram: ', end='')
for n in s:
    print(n, end=', ')
print(f'\nO maior valor sorteado foi: {max(s)}')
print(f'O menor valor sorteado foi: {min(s)}')