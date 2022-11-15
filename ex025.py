# Recebe o nome completo e printa se tem silva ou não o nome
nom=input('Digite o seu nome completo: ').strip()
cap= nom.title()
print('Esse nome tem silva? {}'.format('Silva'in cap))