from Log import *

class AnalisadorLexico:

    aditivos = ['+', '-']
    multiplicativos = ['/', '*']
    chaves = ["program", "var", "integer", "real", "boolean", "procedure", "begin",
              "end", "if", "then", "else", "while", "do", "not", "true", "false"]
    delimitadores = [",", ".", ";", ":", "(", ")", "[", "]"]
    relacionais = ["=", "<", ">", "<=", ">=", "<>"]
    atribuicao = [":="]
    palavra = ""
    linhaCont = 1
    tipoDeClassificadores = ["Palavra Reservada",
                            "Identificador",
                            "Delimitador",
                            "Atribuição",
                            "Número Inteiro",
                            "Aditivos",
                            "Multiplicativos", 
                            "Relacional",
                            "Float"]

    def __init__(self, arquivoInput):
        self.log = Log()
        self.arquivo = open(arquivoInput, "r")

    def clearWord(self):
        self.palavra = ""

    def isFloat(self, value):
        try:
            float(value)
        except ValueError:
            return False
        return True

    def start(self):
        
        for caracter in iter(lambda: self.arquivo.read(1), ''):
            if caracter is '{':
                while caracter is not '}':
                    caracter = self.arquivo.read(1)
            elif caracter is ' ' or caracter is '\t':
                self.separa(self.palavra)
            elif caracter is '\n':
                self.linhaCont += 1
                self.separa(self.palavra)
            else:
                self.palavra += caracter
        self.separa(self.palavra)

        self.log.printLog()


    def separa(self, word):

        if word is not "":
            word = word.lower()
            alfabeto = ""
            simbolos = ""
            ultimoCaracter = ""
            flagSimbolo = 0

            for caracter in word:
                print(caracter)
                if not flagSimbolo:
                    if caracter.isalpha():
                        alfabeto += caracter
                        ultimoCaracter = caracter
                    elif (caracter.isdigit() or caracter is '_'):
                        alfabeto += caracter
                        ultimoCaracter = caracter
                    elif alfabeto.isdigit() and caracter is '.':
                        alfabeto += caracter
                    else:
                        self.classifica(alfabeto)
                        print(alfabeto)
                        alfabeto = ""
                        flagSimbolo = 1
                
                if flagSimbolo:
                    simbolos += caracter
                    if( ultimoCaracter.isalpha() or ultimoCaracter.isdigit() or ultimoCaracter is '_' and len(simbolos) >= 1):
                        self.classifica(simbolos)
                        simbolos = ""
                    flagSimbolo = 0
            self.classifica(alfabeto)
        self.clearWord()


    def classifica(self, word):

        if word is not "":
            if word in self.chaves:
                self.log.addLog( word, self.tipoDeClassificadores[0], self.linhaCont)
            elif word.isdigit():
                self.log.addLog( word, self.tipoDeClassificadores[4], self.linhaCont)
            elif word in self.delimitadores:
                self.log.addLog( word, self.tipoDeClassificadores[2], self.linhaCont)
            elif word in self.atribuicao:
                self.log.addLog( word, self.tipoDeClassificadores[3], self.linhaCont)
            elif word in self.aditivos:
                self.log.addLog( word, self.tipoDeClassificadores[5], self.linhaCont)
            elif word in self.multiplicativos:
                self.log.addLog( word, self.tipoDeClassificadores[6], self.linhaCont)
            elif word in self.relacionais:
                self.log.addLog( word, self.tipoDeClassificadores[7], self.linhaCont)
            elif self.isFloat(word):
                self.log.addLog( word, self.tipoDeClassificadores[8], self.linhaCont)
            else:
                self.log.addLog( word, self.tipoDeClassificadores[1], self.linhaCont)


# TO DO
# -> validar número de ponto flutuante
# -> validar linha 
