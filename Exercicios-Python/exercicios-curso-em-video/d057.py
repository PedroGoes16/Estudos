s = input('Digite seu sexo [M/F]: ').strip().upper()[0]
while s not in 'MmFf':
    s = input('Dado inválido. Por favor, informe seu sexo [M/F]:').strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')
print('FIM!')