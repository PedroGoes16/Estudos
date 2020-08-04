from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro valor: '))
n = 6
while n!=5:
    print(20*'-=')
    print(f'\033[1;33mVocê digitou {n1} e {n2}.\033[m')
    n = int(input('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA\nEscolha uma opção: '))
    if n == 1:
        print(f'A SOMA de {n1} e {n2} é igual a {n1+n2}.')
    if n == 2:
        print(f'O PRODUTO de {n1} e {n2} é igual a {n1*n2}.')
    if n == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, {n1} é MAIOR.')
        if n1 == n2:
            print(f'NÃO exite um MAIOR, pois {n1} é igual a {n2}.')
        if n2 > n1:
            print(f'Entre {n1} e {n2}, {n2} é MAIOR.')
    if n == 4:
        n1 = int(input('Digite um NOVO NÚMERO: '))
        n2 = int(input('Digite outro NOVO NÚMERO: '))
    if n < 1 or n > 5:
        print('Você digitou uma opção invalida, tente novamente ;-)')
    sleep(2)
print('\033[32mObrigado por utilizar meus serviços!!!\033[m')