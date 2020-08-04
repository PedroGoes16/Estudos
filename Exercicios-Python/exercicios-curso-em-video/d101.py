def voto(n):
    from datetime import date
    i = date.today().year - n
    print(f'Com {i} anos: ',end='')
    if 18<=i<65:
        print('VOTO OBRIGATÓRIO.')
    elif 16 <= i < 18 or i>=65:
        print('VOTO OPCIONAL.')
    else:
        print('NÃO VOTA.')


print(30*'-')
ano = int(input('Em que ano você nasceu? '))
voto(ano)