print(30*'=')
print('       BANCO DO PEDRÃO')
print(30*'=')
v = int(input('Qual valor você quer sacar? R$'))
while True:
    if v >= 50:
        nc = v//50
        v -=50*nc
        print(f'Total de {nc} cédulas de R$50,00.')
    if v >= 20:
        nv = v//20
        v -=20*nv
        print(f'Total de {nv} cédulas de R$20,00.')
    if v >= 10:
        nd = v//10
        v-= 10*nd
        print(f'Total de {nd} cédulas de R$10,00.')
    if v >=1:
        print(f'Total de {v} cédulas de R$1,00.')
        break
print(30*'=')
print('Volte sempre ao BANCO DO PEDRÃO! Tenha um bom dia!')
