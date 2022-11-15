import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    print('O site Pudim não está disponível no momento')
else:
    print('tudo ok, o site está disponível.')
    print(site.read())