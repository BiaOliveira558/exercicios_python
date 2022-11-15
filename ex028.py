# Recebe um numero enquanto o computador gera
# um aleatorio entre 0 e 5 e se o numero digitado
# for igual o escolhido vai ser printada
# uma mensagem se não outra mensagem é printada e
# depois printa o numero gerado pelo computador
import random
from time import sleep
escolhido=int(random.randint(0,5))
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar... ')
print('-=-'*20)
n=int(input('Tente adivinhar o número inteiro entre 0 a 5 escolhido pelo computador: '))
print('PROCESSANDO...')
sleep(3)
if n==escolhido:
    print('Você venceu')
else:
    print('Você perdeu')
print('O número escolhido pelo computador foi {}'.format(escolhido))