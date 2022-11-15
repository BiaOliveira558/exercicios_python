#fatorial com while

num = int(input('Digite um número para saber seu fatorial: '))
contador = num
fatorial = 1
print('Fatorial de {}! = '.format(num), end='')
while contador > 0:
    print('{} '.format(contador),end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial* contador
    contador-=1
print('{}'.format(fatorial))

# fatorial com for

'''num = int(input('Digite um número para saber seu fatorial: '))
contador = 1
print('{}! = '.format(num),end='')
for c in range (num,0,-1):
    print(c,end='')
    print(' x ' if c > 1 else ' = ',end='')
    contador = contador* c
print(contador)'''
