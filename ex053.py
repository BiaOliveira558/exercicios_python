frase=str(input('Digite uma frase: ')).upper(). strip().split()
junção=''.join(frase)
inverso=''
for c in range (len(junção)- 1,-1,-1):
    inverso+=junção[c]
print('O inverso de {} é {}'.format(junção,inverso))
if inverso==junção:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
# solução sem o for
# inverso= junto[::-1]