print('\033[1;30;41m',20*'+-','\033[m')
print('\033[1;31;40m','            RESULTADO FINAL!            ','\033[m')
print('\033[1;30;41m',20*'+-','\033[m')
n1 = float(input('Insira a primeira nota de um aluno: '))
n2 = float(input('Insira a segunda nota desse aluno: '))
m = (n1+n2)/2
if m < 5:
    print(f'A média deste aluno foi de {m:.1f} pontos!\nPortanto está \033[1;31mREPROVADO\033[m!!!')
elif 5<=m<6.9:
    print(f'A média deste aluno foi de {m:.1f} pontos!\nPortanto está de \033[1;33mRECUPERAÇÃO\033[m!!!')
else:
    print(f'A média deste aluno foi de {m:.1f} pontos!\nPortanto está \033[1;32mAPROVADO\033[m!!!')
