print(30*'=')
print('    10 TERMOS DE UMA P.A.')
print(30*'=')
p = int(input('Digite o primeiro termo de uma P.A.: '))
r = int(input('Digite a razão dessa P.A.: '))
for c in range(p, r*10+p, r):
    print(c, end=' -> ')
print('ACABOU!')