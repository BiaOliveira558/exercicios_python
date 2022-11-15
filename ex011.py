# recebe dois valores um de altura e largura e depois printa a área e quantas latas de tintas podem ser usadas para pintar
a = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
print('A área dessa parede é {:.1f} metros quadrados, e precisará de {:.1f} litros de tinta'.format( a*l, (a*l)/2 ))
