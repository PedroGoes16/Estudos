from random import shuffle
from time import sleep
l = ['PEDRA', 'PAPEL', 'TESOURA']
shuffle(l)
print('\033[1;33;41m', 20*'@#','\033[m')
print('\033[1;31;43m', '                JOKENPÔ                 ','\033[m')
print('\033[1;33;41m', 20*'@#', '\033[m')
print('\033[1;31;43m   Te desafio a jogar Jokenpô comigo!!!   \033[m')
j = input('\033[1;33;41m         Pedra, papel ou tesoura?         \033[m\n')
print('\033[1;31;43m                    JO                    \033[m')
sleep(1)
print('\033[1;33;41m                    KEN                   \033[m')
sleep(1)
print('\033[1;31;43m                    PÔ!!!                 \033[m')
sleep(1)
j = j.upper()
j = j.split()
print(f'\033[1;33m              {j[0]}\033[m vs \033[1;34m{l[0]}\033[m             ')
if j[0] == l[0]:
    print(f'Você escolheu \033[1;33m{j[0]}\033[m e eu também \033[1;34m{l[0]}\033[m, então empatamos ;-) ')
elif j[0] == 'PAPEL' and l[0] == 'PEDRA' or j[0] == 'TESOURA' and l[0] == 'PAPEL' or j[0] == 'PEDRA' and l[0] == 'TESOURA':
    print(f'Você escolheu \033[1;33m{j[0]}\033[m e eu \033[1;34m{l[0]}\033[m, infelizmente eu \033[1;31mPERDI\033[m :-( ')
elif j[0] == 'PAPEL' and l[0] == 'TESOURA' or j[0] == 'TESOURA' and l[0] == 'PEDRA' or j[0] == 'PEDRA' and l[0] == 'PAPEL':
    print(f'Você escolheu \033[1;33m{j[0]}\033[m e eu \033[1;34m{l[0]}\033[m, então \033[1;32mGANHEI\033[m!!! Foi moleza essa! ;-)')
else:
    print('Jogada inválida! Jogue novamente ;-)')