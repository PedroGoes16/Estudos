print('\033[1;33;41m', 20*'ΔΔ','\033[m')
print('\033[1;31;43m', '        ANALISADOR DE TRIÂNGULOS        ', '\033[m')
print('\033[1;33;41m', 20*'ΔΔ', '\033[m')
s1 = float(input('Insira o comprimeto de um segmento de reta: '))
s2 = float(input('Insira o segundo: '))
s3 = float(input('E por fim, insira o terceiro: '))
if s1 + s2 < s3 or s1 + s3 < s2 or s2 + s3 < s1:
    print(f'Com os segmentos {s1}, {s2} e {s3}, não é possível formar um triângulo :-(')
else:
    if s1 == s2 == s3:
        print(f'Com os segmentos {s1}, {s2} e {s3}, formaremos um triângulo EQUILÁTERO!')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print(f'Com os segmentos {s1}, {s2} e {s3}, formaremos um triângulo ESCALENO!')
    else:
        print(f'Com os segmentos {s1}, {s2} e {s3}, formaremos um triângulo ISÓCELES!')