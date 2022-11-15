lista=[]
for c in range(1,6):
    peso=float(input('Digíte o peso da {} pessoa: '.format(c)))
    lista+=[peso]
print('O maior peso lido foi {}'.format(max(lista)))
print('O menor peso lido foi {}'.format(min(lista)))