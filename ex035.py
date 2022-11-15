# Recebe tres valores e checa se da pra formar um triangulo ou não

l1=float(input('Digite o primeiro segmento: '))
l2=float(input('Digite o segundo segmento: '))
l3=float(input('Digite o terceiro segmento: '))
if l1 < l2+l3 and l2 < l3+l1 and l3 < l1+l2:
    print('É possível formar esse triângulo')
else:
    print('Não é possível formar esse triângulo')