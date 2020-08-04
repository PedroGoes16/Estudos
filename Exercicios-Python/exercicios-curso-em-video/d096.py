def ar(c,b):
    a = c*b
    print(f'A area de um terreno {c} x {b} é de {a:.1f}m².')


print('   Controle de Terrenos')
print(26*'-')
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
ar(a,b)