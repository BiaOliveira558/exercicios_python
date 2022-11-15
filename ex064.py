cont = 0
soma = 0
num = 0
num = int(input('Digite um número [ 999 para parar ]:  '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [ 999 para parar ]:  '))

print('O total de números que você digitou foi {} e a soma deles é {}'.format(cont,soma))
