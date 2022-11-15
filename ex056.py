somaidade=0
média=0
maioridadehomem=0
nomehomemvelho=0
totmulheresmenosvinte=0
for c in range(1,5):
    print('{} PESSOA'.format(c))
    nome=str(input('Qual o seu nome? ')).strip().lower()
    idade=int(input('Qual a sua idade? '))
    sexo=str(input('Sexo [M/F]: ')).upper()
    somaidade+=idade
    if c==1 and sexo=='M':
        maioridadehomem=idade
        nomehomemvelho=nome
    if sexo=='M' and idade>maioridadehomem:
        maioridadehomem=idade
        nomehomemvelho=nome
    if sexo=='F' and idade<20:
         totmulheresmenosvinte+=1
média=somaidade/4
print('A média das idades será {:.2f}'.format(média))
print('O nome do homem mais velho é {} com a idade de {} anos '.format(nomehomemvelho,maioridadehomem))
print('{} é o número de mulheres com menos de 20 anos'.format(totmulheresmenosvinte))