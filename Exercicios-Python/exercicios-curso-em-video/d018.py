import math
an = float(input('Digite o angulo que você deseja: '))
print(f'O angulo {int(an)}°, possui:\nSeno = {math.sin(math.radians(an)):.2f}\nCosseno = {math.cos(math.radians(an)):.2f}\nTangente = {math.tan(math.radians(an)):.2f}')