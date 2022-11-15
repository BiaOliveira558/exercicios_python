# programa que recebe o valor de uma compra e calcula o valor que ficara dependendo do pagamento
preço=float(input('Digíte o preço das compras: R$ '))
print('FORMAS DE PAGAMENTO \n[1] á vista/cheque \n[2] á vista no cartão \n[3] em até 2x no cartão\n[4] 3x ou mais no cartão')
pagamento=int(input('Qual a forma de pagamento? '))

if pagamento==1:
    print('Á vista no dinheiro ou cartão sua compra ficará: {:.2f}'.format(preço*0.9))
elif pagamento==2:
    print('Á vista no cartão sua compra ficará: {:.2f}'.format(preço*0.95))
elif pagamento==3:
    print('Em até 2x no cartão o preço continuará {:.2f} com parcelas de {:.2f} mensal'.format(preço,preço/2))
elif pagamento==4:
    print('Em 3x ou mais no cartão o preço ficará: {:.2f}'.format(preço*1.20))
    parcela= int(input('Quantas parcelas? '))
    print('As parcelas a pagar serão no valor de {:.2f}'.format((preço*1.2)/parcela))
else:
    print('\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE')
