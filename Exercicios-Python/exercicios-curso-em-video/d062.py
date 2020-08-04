print('\n',30*'=','\n', '      TERMOS DE UMA P.A.\n', 30*'=')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
m = 10
while c < m:
    if c == 0:
        print(f'P.A. = ', end = '')
    k = p + c * r
    print(k, end=' -> ')
    c += 1
    if m == c:
        print('PAUSA')
        mais = int(input('Deseja ver mais quantos termos? '))
        m = m+mais
print(f'Progressão finalizada com {m} termos mostrados.')