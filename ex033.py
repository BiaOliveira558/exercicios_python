# recebe tres numeros e printa qual é o maior e o menor

a=int(input('Digíte um número: '))
b=int(input('Digite outro número: '))
c=int(input('Digíte outro número: '))
#lista=[a,b,c]
#print('O número máximo é {} e o mínimo é {}'.format(max(lista),min(lista)))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>b and c>a:
    maior=c
print('O maior número é {} e o menor {}'.format(maior,menor))