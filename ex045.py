# programa de pedra papel e tesoura
from time import sleep
import random
itens= ('Pedra','Papel','Tesoura')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada=int(input('Qual é a sua jogada? '))
if jogada!=0 and jogada!= 1 and jogada!=2:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
else:
    comp= random.randint(0,2)
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('='*24)
    print('''Computador jogou {}\nJogador jogou {}'''.format(itens[comp],itens[jogada]))
    print('='*24)
    if jogada==0 and comp==2 or jogada==2 and comp==1 or jogada==1 and comp==0:
        print('JOGADOR VENCE')
    elif comp==0 and jogada==2 or comp==2 and jogada==1 or comp==1 and jogada==0:
        print('COMPUTADOR VENCE')
    elif comp==jogada:
        print('EMPATE')


