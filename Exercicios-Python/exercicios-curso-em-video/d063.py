n = int(input('Quantos termos você quer da sequencia de Fibonacci: '))
f = []
c = 0
while c < n:
    c+=1
    if c == 1:
        f.append(0)
    if c == 3 or c == 2:
        f.append(1)
    if c > 3:
        p = f[c-3] + f[c-2]
        f.append(p)
print(f)