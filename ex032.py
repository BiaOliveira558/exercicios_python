# Recebe um ano e checa se é bissexto ou não

#import calendar
from datetime import date
ano=int(input('Digite o ano que você quer analisar, se quiser analisar o ano atual coloque 0: '))

#if calendar.isleap(ano)== True:
    #print('Esse ano é bissexto')
#else:
    #print('Esse ano não é bissexto')
if ano==0:
    ano=date.today().year
if ano/4== ano//4 and ano/100 != ano//100 or ano/4==ano//4 and ano/100==ano//100 and ano/400==ano//400:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
