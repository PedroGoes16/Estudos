def e(t):
    print((len(t)+4)*'~')
    print(f'  {t}  ')
    print((len(t)+4)*'~')

from time import sleep
while True:
    print('\033[7;32;40m', end='')
    e('SISTEMA DE AJUDA PyHELP')
    print('\033[m', end='')
    f = input('Função ou Biblioteca (termine com FIM) > ').strip().lower()
    if f == 'fim':
        sleep(2)
        break
    print('\033[7;34;40m',end='')
    e(f"Acessando o manual do comando '{f}'")
    print('\033[m', end='')
    sleep(2)
    print('\033[7;30m', end='')
    help(f)
    print('\033[m', end='')
    sleep(2)
print('\033[7;31;40m', end='')
e('ATÉ LOGO!')

