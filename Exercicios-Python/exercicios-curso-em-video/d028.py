import random
nu = int(input('Pensei num número de 0 a 5, tente adivínhar! '))
n = random.randrange(5)
if n == nu:
    print(f'Voce venceu! Escolhi o número {n}!')
else:
    print(f'Voce perdeu! Escolhi o número {n}!')