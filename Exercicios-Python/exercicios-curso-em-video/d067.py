while True:
    n = int(input('Quer ver a tabuada de qual valor?[P/ finalizar digite um valor negativo] '))
    print(75*'=')
    if n<0:
        print('Obrigado por utilizar meus serviços de tabuada!!!\n\033[1;32mVolte sempre ;-)')
        break
    c = 1
    while c<=10:
        print(f'{n} x {c} = {n*c}')
        c+=1
    print(75*'=')