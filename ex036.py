# Recebe valores e dependendo desses valores printa se pode financiar uma casa ou não
valorcasa= float(input('Qual o valor da casa que você quer financiar: '))
salário=float(input('Qual o seu salário: '))
anos= int(input('Em quantos anos você pretende pagar essa casa: '))
prestação= valorcasa/(anos*12)
print('O valor da prestação será: {:.2f} '.format(prestação))
if prestação > salário*0.3:
    print('E de acordo com seu salário você não poderá financiar essa casa')
else:
    print('O empréstimo é viável')