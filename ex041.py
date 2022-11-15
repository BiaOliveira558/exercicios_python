# programa que calcula em que categoria uma pessao está dependendo da idade recebida
from datetime import date
ano=int(input('Digite o ano de seu nascimento: '))
idade= date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade<= 9:
    print('MIRIM')
elif 9<idade<=14:
    print('INFANTIL')
elif 14<idade<=19:
    print('JÚNIOR')
elif 19<idade<=25:
    print('SÊNIOR')
elif idade>25:
    print('MASTER')
