from datetime import date
d = {}
d['Nome'] = input('Nome: ')
a = int(input('Ano de Nascimento: '))
d['Idade'] = date.today().year - a
d['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if d['CTPS'] != 0:
    d['Contratação'] = int(input('Ano de contratação: '))
    d['Salário'] = float(input('Salário: R$'))
    d['Aposentadoria'] = (d['Contratação'] + 35) - a
print(30*'-=')
for c,v in d.items():
    print(f'{c} tem o valor {v}.')