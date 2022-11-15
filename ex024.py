# Recebe um numero e printa se tem a palavra santo ou não no nome
nom = input('Digite o nome da sua cidade: ').strip().split()
p=nom[0].upper()
print('A sua cidade tem santo no nome? {}'.format('SANTO'in p ))

#cid=str(input('Em que cidade você nasceu? ')).strip()
#print(cid[:5].upper() =='SANTO')