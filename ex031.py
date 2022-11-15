# recebe uma distancia
# se essa distancia for maior ou igual a 200
# printa uma mensagem
# se não
# printa outra

km=float(input('Digite a distância,em km, da sua viagem: '))
if km <= 200:
    print('Pra essa viagem você pagará {} reais'.format(km*0.50))
else:
    print('Pra essa viagem você pagará {} reais'.format(km*0.45))
#preço= km*0.50 if km <=200 else km* 0.45