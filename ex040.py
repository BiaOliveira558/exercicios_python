# programa para checar se um aluno passou, reprovou ou esta de recuperação
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('Sua média será {:.1f}'.format(média))
if média < 5:
    print('REPROVADO')
elif 5 <= média <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
