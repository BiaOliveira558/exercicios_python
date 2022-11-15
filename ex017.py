# importando uma biblioteca; recebe um valor de um cateto e depois o valor de outro, calcula o valor da hipotenusa e printa ele.
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#hip = math.sqrt(co ** 2 + ca ** 2)
#print('O valor da hipotenusa do triângulo retangulo de catetos {} e {} é {:.2f}'.format(co, ca, hip))
hip = math.hypot(co,ca)
print('O valor da hipotenusa é: {:.2f}'.format(hip))
