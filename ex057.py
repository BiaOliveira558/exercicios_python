
resposta = str(input('Digite o seu sexo [F/M]: ')).upper().strip()

while resposta != 'M' and resposta !="F":
    resposta = str(input('Dado errado, digite F para feminino ou M para masculino: ')).upper().strip()

print('Sexo {} registrado'.format(resposta))
