b = 'Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético Mineiro', 'Botafogo', 'Atlético Paranaense', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético Goianiense'
print(30*'-=')
print(f'Classificação do Brasileirão 2017: {b}')
print(30*'-=')
print(f'Os 5 primeiros são: {b[:5]}')
print(30*'-=')
print(f'Os 4 últimos são: {b[-4:]}')
print(30*'-=')
print(f'Times em ordem alfabética: {sorted(b)}')
print(30*'-=')
pc = b.index('Chapecoense')+1
print(f'A Chapecoense está na {pc}ª posição.')
