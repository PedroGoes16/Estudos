d = float(input('Qual a distância dessa viagem em Km? '))
if d <= 200:
    p = d*0.5
    print(f'O preço da passagem dessa viagem é R${p:.2f}.')
else:
    p = d*0.45
    print(f'O preço da passagem dessa viagem é R${p:.2f}.')
