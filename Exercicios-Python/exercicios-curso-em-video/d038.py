print('\033[7;30m',21*'#','\033[m')
print('\033[1;31;40m','COMPARADOR DE NÚMEROS','\033[m')
print('\033[7;30m',21*'#','\033[m')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1>n2:
    print(f'O primeiro valor, {n1}, é maior!')
elif n2>n1:
    print(f'O segundo valor, {n2}, é maior!')
else:
    print(f'Não existe valor maior {n1} é igual a {n2}')