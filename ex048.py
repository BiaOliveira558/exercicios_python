# calcula a soma dos impares dos multiplos de 3 entre 1 e 500
s = 0
cont=0
for c in range(0,501):
    if c %3==0 and c% 2!=0:
        s += c
        cont =cont+1
print('A soma dos {} números ímpares, múltiplos de 3 entre 1 e 500 é {}'.format(cont,s))