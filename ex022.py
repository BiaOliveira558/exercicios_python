# Recebe um nome, printa ele em letras maiusculas, minusculas, o total de letras do nome completo e o total do primeiro nome.
nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} ao total'.format(len(nome) - nome.count(' ')))
div = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(div[0])))


