print('\033[1;32;44m', 20*'=+', '\033[m')
print('\033[1;34;42m', '        ÍNDICE DE MASSA CORPORAL        ', '\033[m')
print('\033[1;32;44m', 20*'=+', '\033[m')
p = float(input('Qual o seu peso? (kg) '))
a = float(input('Qual a sua altura? (m) '))
i = p/a**2
print(f'Seu IMC é {i:.2f} e seu status é: ',end='')
if i < 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 <= i < 25:
    print('PESO IDEAL!')
elif 25 <= i < 30:
    print('SOBREPESO!')
elif 30 <= i < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')