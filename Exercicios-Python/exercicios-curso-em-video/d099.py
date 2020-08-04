from time import sleep
def maior(*lst):
    print(30*'-=')
    print('Analisandos os valores passados ...')
    for v in lst:
        print(v,end=' ')
    print(f'Foram informado {len(lst)} valores ao todo.')
    if len(lst) > 0:
        print(f'O maior valor informado foi {max(lst)}.')
    else:
        print('O maior valor informado foi 0.')
    sleep(2)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()