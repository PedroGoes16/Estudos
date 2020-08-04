v = int(input('Qual a velocidade do carro em Km/h? '))
if v > 80:
    e = v - 80
    m = e*7
    print(f'Você foi multado em R${m:.2f} por excesso de velocidade em {e}Km/h acima do permitido que é 80Km/h!')
else:
    print(f'Você não foi multado! Pois {v}Km/h é uma velocidade permitida!')