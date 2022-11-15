# Usando função de uma biblioteca, recebe um valor e printa a porção inteira do numero
from math import trunc
num = float(input('Digite um número '))
print('A porção inteira desse número é {}'.format(trunc(num)))