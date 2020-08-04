import datetime
s = int(datetime.date.today().year)
ma = 0
me = 0
for c in range(1,8):
    n = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if s - n < 21:
        me+=1
    else:
        ma+=1
print(f'{ma} pessoa(s) já é(são) maiore(s) de idade, enquanto {me} pessoa(s) é(são) menor(es) de idade.')