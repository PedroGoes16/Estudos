from random import shuffle
a = input('Quais alunos irão apresentar trabalhos? ').split(', ')
shuffle(a)
print(f'A ordem de apresentação será 1° {a[0]}, 2° {a[1]}, 3° {a[2]} e 4° {a[3]}!')
