l = []
for i in range(0,5):
    v = int(input('Digite um valor: '))
    if l != [] and v < max(l):
        c=0
        for n in l:
            if v>n:
                c+=1
        l.insert(c,v)
        print(f'Adicionado na posição {c} da lista...')
        print(30*'-=')
    if l == [] or v > max(l):
        l.append(v)
        print('Adicionado ao final da lista...')
        print(30*'-=')
print(f'Os valores digitados em ordem foram {l}.')