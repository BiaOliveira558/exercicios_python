# programa que calcula o imc e checa em que categoria a pessoa se encaixa
peso=float(input('Digite o seu peso: '))
altura=float(input('Digite a sua altura: '))
imc= peso/(altura)**2
print('Seu imc é {:.1f}'.format(imc))
if imc<18.5:
    print('Você está abaixo do peso')
elif 18.5<= imc<25:
    print('Você está no peso ideal')
elif 25<=imc<30:
    print('Você está com sobrepeso')
elif 30<=imc<40:
    print('Você está obeso')
elif imc>= 40:
    print('Você está com obesidade mórbida')
