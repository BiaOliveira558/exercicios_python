# programa para checar se uma pessoa esta na idade de se alistar ou não
from datetime import date
ano=int(input('Digite o ano de seu nascimento: '))
idade= date.today().year - ano
if idade == 18:
    print('É hora de se alistar')
elif idade < 18:
    print('Ainda faltam {} anos pra você se alistar; '
          'você se alistará em {}'.format(18-idade,(18-idade)+date.today().year))
else:
    print('Passou {} anos do seu alistamento, '
          'você deveria ter se alistado em {}'.format(idade-18,date.today().year-(idade-18)))