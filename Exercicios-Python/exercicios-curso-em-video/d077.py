palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
for p in palavras:
    p1=p
    print(f'\nNa palavra {p1.upper()} temos: ', end='')
    for v in p1:
        if v in 'aeiou':
            print(v, end=', ')