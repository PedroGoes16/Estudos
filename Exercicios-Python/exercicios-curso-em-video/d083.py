e = input('Digite a expressão: ')
pa = pf = 0
for c in e:
    if c == '(':
        pa+=1
    if c == ')':
        pf+=1
if pa == pf:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')