import moeda
preço = float(input('Digite o preço: '))
print(f'A metade de {preço} é {moeda.metade(preço):.2f}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10% de {preço} temos {moeda.aumenta10(preço,10)}')
print(f'Reduzindo 13% de {preço} temos {moeda.reduz13(preço,13)}')