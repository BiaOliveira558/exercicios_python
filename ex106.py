while True:
    resposta = str(input('Digite uma biblioteca ou função: '))
    if resposta.strip().lower() == 'fim':
        break
    help(resposta)
