from time import sleep
def con(i,f,p):
    if p < 0:
        p = p - p - p
    if p == 0:
        p = 1
    print(25*'-=')
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i < f:
        for n in range(i,f+1,p):
            sleep(1)
            print(n, end=' ')
        sleep(0.5)
        print('FIM!')
    else:
        for n in range(i,f-1,-p):
            sleep(1)
            print(n, end=" ")
        sleep(0.5)
        print('FIM!')


con(1,10,1)
con(10,0,2)
print(25*'-=')
print('Agora é a sua vez de personalizar a contagem! ')
i = int(input('Início: '))
f = int(input(f'{"Fim:":<8}'))
p = int(input(f'{"Passo:":<8}'))
con(i,f,p)