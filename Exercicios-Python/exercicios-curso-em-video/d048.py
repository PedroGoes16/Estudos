s = 0
co = 0
for c in range(1,500,2):
    if c%3==0:
        co += 1
        s += c
print(f'A entre todos os {co} números ímpares que são múltiplos de 3, de 1 até 500 é igual a {s}.')