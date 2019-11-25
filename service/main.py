from Lexico import *
from Sintatico import *

test = AnalisadorLexico("arquivo.txt")
log = test.start()
log[1].printLog(log)

sintatico = AnalisadorSintatico(log)
print(sintatico.programa())
