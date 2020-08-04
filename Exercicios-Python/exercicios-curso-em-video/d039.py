import datetime
s = datetime.date.today().year
s = int(s)
print('\033[1;33;44m',20*'-=','\033[m')
print('\033[1;34;43m','        FORÇAS ARMADAS DO BRASIL        ','\033[m')
print('\033[1;33;44m',20*'-=','\033[m')
n = int(input('Qual seu ano de nascimento jovem? '))
i = s - n
p = n + 18
if i < 18:
    print(f'Você tem {i} anos e ainda vai se alistar ao serviço militar!\nSerá no ano de {p} e ainda falta(m) {p-s} ano(s)')
elif i == 18:
    print(f'Você tem {i} anos e {s} já é o ano de seu alistamento, fique atento!')
else:
    print(f'Você tem {i} anos e já passou em {s-p} ano(s) do prazo de alistamento!\nSeu alistamento era para ser feito em {p}!\nRegularize sua situação!')