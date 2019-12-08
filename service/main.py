from Lexico import *
from Syntactic import *

test = AnalisadorLexico("arquivo.txt")
log = test.start()
log[1].printLog(log)

sintatico = Syntactic(log)
print(sintatico.programa())
