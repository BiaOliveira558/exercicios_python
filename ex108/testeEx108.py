from ex108 import moeda
preço = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10% de {moeda.moeda(preço)} temos {moeda.moeda(moeda.aumenta10(preço,10))}')
print(f'Reduzindo 13% de {moeda.moeda(preço)} temos {moeda.moeda(moeda.reduz13(preço,13))}')