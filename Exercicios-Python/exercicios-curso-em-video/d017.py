import math
co = float(input('Digite o comprimento do catedo oposto de um triângulo retangulo: '))
ca = float(input('Digite o comprimento do cateto adjascente desse triângulo: '))
h = math.sqrt(co**2+ca**2)
print(f'A hipotenusa de um triangulo com cateto oposto {co} e cateto adjascente {ca} terá um comprimento de {h}.')