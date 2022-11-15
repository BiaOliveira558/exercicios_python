def metade(num = 0):
    met = num/2
    return  met
def dobro(num = 0):
    dob = num * 2
    return dob
def aumenta10(num = 0 ,taxa = 0):
    aum = num + (num * taxa/100)
    return aum
def reduz13(num = 0 ,taxa = 0 ):
    red= - num * ((taxa/100) - 1)
    return red
def moeda(num = 0 ,moeda = 'R$'):
    return f'{moeda}{num}'.replace('.',',')