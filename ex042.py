# programa que calcula se um triangulo é equilatero, escaleno ou isosceles dependendo do valor dos lados do triangulo
a =float(input('Primeiro segmento: '))
b =float(input('Segundo segmento: '))
c =float(input('Terceiro segmento: '))
if a<b+c and b<a+c and c<a+b:
    print('É POSSIVEL formar um triângulo',end='')
    if a==b==c:
        print(' EQUILÁTERO')
    elif a != b!= c !=a :
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('NÃO É POSSÍVEL formar triângulo')


