from random import randint
print(15*'=-','\nVAMOS JOGAR PAR OU ÍMPAR')
print(15*'=-')
vi = 0
while True:
    v = int(input('Diga um valor: '))
    e = 'a'
    while e not in 'PI':
        e = input('Par ou Ímpar?[P/I] ').strip().upper()[0]
    print(30*'-')
    c = randint(0, 10)
    t = c+v
    print(f'Você jogou {v} e o computador {c}. Total de {v + c}', end=' ')
    print('DEU PAR' if t%2==0 else 'DEU ÍMPAR')
    print(30*'=')
    if e == 'P':
        if t%2==0:
            print('Você GANHOU!')
            vi+=1
        else:
            print('Você PERDEU!')
            break
    if e == 'I':
        if t%2==1:
            print('Você GANHOU!')
            vi+=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print(15*'=-')
print(f'\033[1;31mGAME OVER!\033[m Você venceu {vi} vezes.')