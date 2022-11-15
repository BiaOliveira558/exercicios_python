# recebe seis numeros inteiros e printa a soma dos pares
s=0
for c in range (1,7):
    num = int(input('Digíte seis números inteiros: '))
    if num%2==0:
        s = s+num
print('A soma dos pares será {}'.format(s))



