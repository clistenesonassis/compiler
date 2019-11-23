from Log import *

class AnalisadorLexico:

    aditivos = ['+', '-']
    multiplicativos = ['/', '*']
    chaves = ["program", "var", "integer", "real", "boolean", "procedure", "begin",
              "end", "if", "then", "else", "while", "do", "not", "true", "false"]
    inteiros = []  # type: List(str)
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
                            "Relacional"]

    def __init__(self, arquivoInput):
        self.log = Log()
        self.arquivo = open(arquivoInput, "r")

    def clearWord(self):
        self.palavra = ""

    def start(self):
        
        for caracter in iter(lambda: self.arquivo.read(1), ''):
            if caracter is '{':
                while caracter is not '}':
                    caracter = self.arquivo.read(1)
            elif caracter is ' ' or caracter is '\t':
                self.Classifica()
            elif caracter is '\n':
                self.linhaCont += 1
                self.Classifica()
            else:
                self.palavra += caracter
        self.Classifica()

        self.log.printLog()

    def Classifica(self):

        if self.palavra is not "":
            self.palavra = self.palavra.lower()
            alfabeto = ""
            simbolos = ""

            for caracter in self.palavra:
                if caracter.isalpha():
                    alfabeto += caracter
                else:
                    if caracter.isdigit() or caracter is '_':
                        alfabeto += caracter
                    else:
                        simbolos += caracter

            if alfabeto is not "":
                if alfabeto in self.chaves:
                        self.log.addLog( alfabeto, self.tipoDeClassificadores[0], self.linhaCont)
                elif alfabeto.isdigit():
                    self.log.addLog( alfabeto, self.tipoDeClassificadores[4], self.linhaCont)
                else:
                    self.log.addLog( alfabeto, self.tipoDeClassificadores[1], self.linhaCont)

            if simbolos is not "":
                if simbolos in self.delimitadores:
                    self.log.addLog( simbolos, self.tipoDeClassificadores[2], self.linhaCont)
                elif simbolos in self.atribuicao:
                    self.log.addLog( simbolos, self.tipoDeClassificadores[3], self.linhaCont)
                elif simbolos in self.aditivos:
                    self.log.addLog( simbolos, self.tipoDeClassificadores[5], self.linhaCont)
                elif simbolos in self.multiplicativos:
                    self.log.addLog( simbolos, self.tipoDeClassificadores[6], self.linhaCont)
                elif simbolos in self.relacionais:
                    self.log.addLog( simbolos, self.tipoDeClassificadores[7], self.linhaCont)

        self.clearWord()

# TO DO
# -> validar número de ponto flutuante
# -> validar linha 
