# Calcula 10 termos de uma PA
print('='*20)
print('10 termos de uma PA ')
print('='*20)
primeiro=int(input('primeiro termo: '))
razão=int(input('razão: '))
décimo= primeiro + (10-1)*razão
for c in range (primeiro,décimo + razão,razão):
    print('{}'.format(c),end='-')
print('ACABOU')