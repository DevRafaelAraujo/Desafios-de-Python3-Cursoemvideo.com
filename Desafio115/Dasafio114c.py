from interface import menu
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo('cursoemvideo.txt')

menu.principal(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
