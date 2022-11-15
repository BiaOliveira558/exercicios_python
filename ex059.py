from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

print('=-='* 10)
print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
opção = int(input('>'*5+' Qual opção você escolhe: '))
while opção!=5:
   if opção == 1:
       sleep(1)
       print('A soma entre {} + {} = {}'.format(num1,num2,num1+num2))
       sleep(2)
       print('=-=' * 10)
       print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
       opção = int(input('>' * 5 + ' Qual opção você escolhe: '))

   elif opção == 2:
       sleep(1)
       print('A multiplicação entre {} x {} = {} '.format(num1,num2,num1*num2))
       sleep(2)
       print('=-=' * 10)
       print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
       opção = int(input('>' * 5 + ' Qual opção você escolhe: '))

   elif opção == 3:
       sleep(1)
       if num1>num2:
           print('O maior número é o {} '.format(num1))
       elif num2>num1:
           print('O maior número é o {}'.format(num2))
       else:
           print('Não tem valor maior, os dois são iguais')
       sleep(2)
       print('=-=' * 10)
       print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
       opção = int(input('>' * 5 + ' Qual opção você escolhe: '))

   elif opção == 4:
       sleep(1)
       num1 = int(input('Primeiro valor: '))
       num2 = int(input('Segundo valor: '))
       sleep(2)
       print('=-=' * 10)
       print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
       opção = int(input('>' * 5 + ' Qual opção você escolhe: '))
   elif opção==5:
       print('Finalizando...')
   else:
       print('Opção inválida digite novamente')
       sleep(2)
       print('=-=' * 10)
       print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
       opção = int(input('>' * 5 + ' Qual opção você escolhe: '))

print('Finalizando...')
sleep(2)
print('=='* 20 )
print('Fim do programa! Volte sempre!')

#Outra forma de fazer

#from time import sleep
#num1 = int(input('Primeiro valor: '))
#num2 = int(input('Segundo valor: '))
#opção= 0
#while opção != 5:
#    sleep(2)
#    print('''    [1] somar
#    [2] multiplicação
#    [3]maior
#    [4]novos números
#    [5]sair do programa''')
#    opção = int(input('Qual é a sua opção: '))
#    if opção ==1:
#        sleep(1)
#        soma = num1 + num2
#        print('A soma entre {} + {} = {}'.format(num1,num2,soma))
#    elif opção ==2:
#        sleep(1)
#        produto = num1*num2
#        print('O resultado de {} x {} é {}'.format(num1,num2,produto))
#    elif opção == 3:
#        sleep(1)
#        if num1>num2:
#            print('O maior é {}'.format(num1))
#        elif num2> num1:
#            print('O maior é {}'.format(num2))
#        else:
#            print('Os números são iguais')
#    elif opção == 4:
#        sleep(1)
#        print('Informe os números novamente')
#        num1 = int(input('Primeiro valor: '))
#        num2 = int(input('Segundo valor: '))
#    elif opção == 5:
#        print('FINALIZANDO...')
#    else:
#        print('Opção inválida. Tente novamente')
#    print('=-='*10)
#print('Fim do programa')







