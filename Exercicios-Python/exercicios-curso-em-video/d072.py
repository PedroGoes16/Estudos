e = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
n = int(input('Digite um número entre 0 e 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número: '))
    print(f'Você digitou o número {e[n]}.')
    if 0<=n<=20:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        if q in 'S':
            n = int(input('Digite um número entre 0 e 20: '))
        if q in 'N':
            break
print('\nFIM!')