import urllib
import urllib.request
print('========== VERIFICANDO STATUS DE SITE ==========')
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
    print('O site PUDIM está acessível no seu computador')
except:
    print('O site PUDIM não está acessível no seu computador.')