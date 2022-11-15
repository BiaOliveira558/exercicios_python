# recebe uma velocidade
# e se for maior que um valor
# printa uma mensagem
km=float(input('Digite a sua velocidade: '))
if km > 80:
    print('Você foi multado em {} reais'.format((km-80)*7))
print('Tenha um bom dia e dirija com segurança')