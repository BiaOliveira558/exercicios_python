# importando uma biblioteca; recebe o valor de um angulo calcula o cosseno e tangente e printa os tres
import math
ang = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ang))
print('O valor do seno: {:.2f}'.format(seno))
cosseno = math.cos(math.radians(ang))
print('O valor do cosseno é {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(ang))
print('O valor da tangente é {:.2f}'.format(tangente))
#pode tirar as referencias á math



