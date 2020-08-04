fii = input('Digite uma frase: ')
fii = fii.strip()
fi = fii.lower()
fi = fi.replace(' ','')
f = list(fi)
f.reverse()
f = ''.join(f)
print(f'O inverso de {fi.upper()} é {f.upper()}.')
if f == fi:
    print(f'A frase: \033[1;33m{fii}\033[m\nÉ um PALÍNDROMO!!!')
else:
    print(f'A frase: \033[1;33m{fii}\033[m\nNÃO é um PALÍNDROMO!!!')