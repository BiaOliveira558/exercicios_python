# Receb uma frase e printa quantas vezes a letra a aparece na 1 posição e na ultima posição
frase=input('Digite uma frase: ').strip()
upper= frase.upper()
print('A letra A aparece {} vezes'.format(upper.count('A')))
print('A primeira letra A aparece na posição {}'.format(upper.find('A')+1))
print('A última letra A aparece na posição {}'.format(upper.rfind('A')+1))