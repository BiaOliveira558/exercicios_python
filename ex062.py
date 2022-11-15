print('Gerador de termos de uma PA')
print('=-='*10)
primeiro= int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador= 1
total = 0
mais=10
while mais != 0:
    total = total+ mais
    while contador<= total:
        print('{}'.format(primeiro),end='-')
        primeiro=primeiro+razao
        contador = contador+1
    mais = int(input('\nQuantos termos você quer mostrar a mais,digite 0 para parar: '))

print('progressão finalizada com {} termos mostrados'.format(total))

