from ex109 import moeda
preço = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço,True)}')
print(f'O dobro de {moeda.moeda(preço)} é {(moeda.dobro(preço,True))}')
print(f'Aumentando 10% de {moeda.moeda(preço)} temos {(moeda.aumenta(preço,10,True))}')
print(f'Reduzindo 13% de {moeda.moeda(preço)} temos {(moeda.reduz(preço,13,True))}')