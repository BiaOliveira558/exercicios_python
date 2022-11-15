cont = int (input('Quantos termos você deseja mostrar: '))
limite= 3
t1 = 0
t2 = 1
print('{} - {} '.format(t1,t2),end='')
while limite <= cont :
   t3 = t1+t2
   print(' - {}'.format(t3),end='')
   t1=t2
   t2=t3
   limite+=1
print(' - fim')