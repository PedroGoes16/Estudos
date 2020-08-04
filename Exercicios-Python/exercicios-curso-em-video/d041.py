import datetime
d = datetime.date.today().year
print('\033[1;33;46m', 20*'-*','\033[m')
print('\033[1;33;46m', '          CATEGORIA DE ATLETA           ', '\033[m')
print('\033[1;33;46m', 20*'-*','\033[m')
d = int(d)
n = int(input('Qual o ano de nascimento do atleta? '))
print(f'O atleta tem {d-n} anos\nCategoria: ', end='')
if d - n <= 9:
    print('MIRIM')
elif 9<d-n<=14:
    print('INFANTIL')
elif 14<d-n<=19:
    print('JUNIOR')
elif 19<d-n<=25:
    print('SÊNIOR')
else:
    print('MASTER')