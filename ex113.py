def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError,TypeError):
            print('Erro: por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return  num


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('Erro: por favor digite um número flutuante válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

num = leiaInt('Digite um número inteiro: ')
numfloat = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num} e o valor real foi {numfloat}')


