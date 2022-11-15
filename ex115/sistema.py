from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    Criararquivo(arq)

while True:
    resposta = menu(['Listar pessoas','Cadastrar pessoas','Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo.')
        break
    else:
        print('ERRO, digite uma opção válida.')