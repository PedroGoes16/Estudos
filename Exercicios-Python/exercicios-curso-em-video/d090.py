a = {}
a['nome'] = input('Nome: ')
a['media'] = float(input(f'Média de {a["nome"]}: '))
print(25*'-=')
print(f' - Nome é igual a {a["nome"]}.')
print(f' - Média é igual a {a["media"]}.')
if 6 <= a ['media'] <7:
    a['situação'] = 'Recuperação'
if a['media'] >= 7:
    a['situação'] = 'Aprovado'
if a['media'] < 6:
    a['situação'] = 'Reprovado'
print(f' - Situação é igual a {a["situação"]}.')