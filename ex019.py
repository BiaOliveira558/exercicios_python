# importando a biblioteca random para gerar numeros aleatorios; recebe o nome de 4 alunos os coloca em uma lista, escolhe um aleatorio dessa lista e printa
import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno:  '))
a4 = str(input('quarto aluno: '))
#print('O aluno escolhido é {}'.format(random.choices( [a1, a2, a3, a4])))
lista = [a1, a2, a3, a4]
escolhido = random.choices(lista)
print('O escolhido é {}'.format(escolhido))

#import random
#nomes= ['ana','jorge','paulo','paula']
#a= random.choices(nomes)
#print('O aluno escolhido será {}'.format(a))