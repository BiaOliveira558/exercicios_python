def metade(num = 0,formato = False):
    met = num/2
    return  met if formato is False else moeda(met)
def dobro(num = 0,formato = False):
    dob = num * 2
    return dob if formato is False else moeda(dob)
def aumenta(num = 0 ,taxa = 0, formato = False):
    aum = num + (num * taxa/100)
    return aum if formato is False else moeda(aum)
def reduz(num = 0 ,taxa = 0,formato = False ):
    red= - num * ((taxa/100) - 1)
    return red if formato is False else moeda(red)
def moeda(num = 0 ,moeda = 'R$'):
    return f'{moeda}{num}'.replace('.',',')