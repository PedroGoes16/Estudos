print('\n',30*'=','\n', '     10 TERMOS DE UMA P.A.\n', 30*'=')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c != 9:
    c+=1
    if c == 1:
        print(f'P.A. = ',p, end = ' -> ')
    print(p + c*r, end=' -> ')
print('FIM!')