from random import randint
n = randint(0,10)
j = int(input('Pensei num número de 0 até 10, consegue adivinhá-lo? '))
c = 1
while n != j:
    if j > n:
        c+=1
        j = int(input('Menos... Tente novamente!\nQual seu palpite? '))
    if j < n:
        c+=1
        j = int(input('Mais... Tente novamente!\nQual seu palpite? '))
print(f'Você acertou com {c} tentativas. PARABÉNS!!!')