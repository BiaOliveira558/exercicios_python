# Recebe 4 nomes os coloca em uma lista e usa a função shuffle que retorna a lista em uma ordem aleatoria
import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem será {}'.format(lista))