# Recebe o valor de dias de aluguel de um carro e os kilometros rodados e printa o valor para pagar
d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros rodados? '))
print('O valor a pagar é {:.2f} '.format(d*60 + km* 0.15))
