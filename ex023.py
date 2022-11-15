# Recebe um numero printa a unidade a dezena a centena e o milhar

#num=input('Digite um número de 0 a 9999: ').strip()
#print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(num[3],num[2],num[1],num[0]))
num=int(input('Informe um número: '))
print('Unidade: {}'.format(num % 10))
print('Dezena: {}'.format(num//10 % 10))
print('Centena {}'.format(num//100 % 10))
print('Milhar: {}'.format(num//1000 % 10))

