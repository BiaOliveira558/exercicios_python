def leiaDinhero(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO \"{entrada}\" é um preço inválido. Tente novamente.')
        else:
            valido = True
            return float(entrada)
