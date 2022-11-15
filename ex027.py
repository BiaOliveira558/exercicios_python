# Recebe o nome completo, digita o primeiro nome e o ultimo
nome=str(input('Digite seu nome completo: ').strip().title().split())
print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu último nome é: {}'.format(nome[-1]))
