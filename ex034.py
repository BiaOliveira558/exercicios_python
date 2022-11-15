# Recebe um salario e dependendo do valor o aumento sera diferente
sal=float(input('Digite seu atual salário: '))
if sal>1200:
    print('O seu salário com aumento será: {}'.format(sal*1.10))
else:
    print('O seu salário com aumento será: {}'.format(sal*1.15))