import random
tentativas= 0
computador= int(random.randint(0,10))
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10, tente adivinhar... ')
print('-=-'*20)
jogador= int(input('Tente adivinhar o número inteiro entre 0 a 10 escolhido pelo computador: '))
if jogador != 1 and jogador!= 2 and jogador!= 3 and jogador!= 4 and jogador!= 5 and jogador!= 6 and jogador!= 7 and jogador!= 8 and jogador!= 9 and jogador!= 10:
    print('Opção inválida, tente novamente')
else:
    while jogador!=computador:
        if jogador> computador:
            jogador = int(input('menos.... tente mais uma vez:  '))
        elif jogador< computador:
            jogador= int(input('mais....tente mais uma vez: '))
        tentativas = tentativas+1

    print('ACERTOUUUUUUU')
    print('Você precisou de {} tentativas para acertar '.format(tentativas))
    print('A escolha do computador {}'.format(computador))
