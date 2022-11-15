import datetime
cont=0
atual=datetime.date.today().year
for c in range (1,8):
    ano=int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if atual-ano >=21:
     cont+= 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('E também tivemos {} menores de idade'.format(7-cont))
