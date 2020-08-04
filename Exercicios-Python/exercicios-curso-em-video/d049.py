n = int(input('Escolha um número para saber a sua tabuada: '))
print('\033[7;30m  TABUADA   \033[m')
print(12*'=')
for c in range(1,11):
    print(f'{n} x {c} = {n*c}')
print(12*'=')