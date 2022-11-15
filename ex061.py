print('='*20)
print('10 termos de uma PA ')
print('='*20)
primeiro=int(input('primeiro termo: '))
razão=int(input('razão: '))
contador= 10
print('Os dez primeiros termos dessa PA é : ',end='')
while contador>0:
    print('{}'.format(primeiro),end=' ')
    primeiro=primeiro+razão
    contador = contador - 1
