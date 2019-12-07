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
                            "Inteiro",
                            "Aditivos",
                            "Multiplicativos", 
                            "Relacional",
                            "Real"]

    def __init__(self, arquivoInput):
        self.log = []
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
                self.separa(self.palavra)
                self.linhaCont += 1
            else:
                self.palavra += caracter
        self.separa(self.palavra)

        return self.log


    def separa(self, word):
        self.clearWord()
        inicio = 0
        texto = ""

        if word is not "":
            while inicio < len(word):

                if word[inicio].isalpha():
                    for i in range(inicio, len(word)):
                        if word[i].isalpha() or word[i].isdigit() or word[i] is '_':
                            texto += word[i]
                        else:
                            inicio = i
                            self.classifica(texto)
                            texto = ""
                            break

                        if i == len(word) - 1:
                            inicio = i
                            self.classifica(texto)
                            texto = ""
                            inicio = i + 1
                            break
                
                elif not(word[inicio].isalpha() or word[inicio].isdigit() or word[inicio] is '_'):
                    for i in range(inicio, len(word)):
                        if not(word[i].isalpha() or word[i].isdigit() or word[i] is '_'):
                            texto += word[i]
                            if texto is ')':
                                inicio = i + 1
                                self.classifica(texto)
                                texto = ""
                                break
                        else:
                            inicio = i
                            self.classifica(texto)
                            texto = ""
                            break
                        
                        if i == len(word) - 1:
                            inicio = i
                            self.classifica(texto)
                            texto = ""
                            inicio = i + 1
                            break

                elif word[inicio].isdigit():
                    for i in range(inicio, len(word)):
                        if word[i].isdigit():
                            texto += word[i]
                        elif word[i] is '.' and word[i+1].isdigit():
                            texto += word[i]
                        else:
                            inicio = i
                            self.classifica(texto)
                            texto = ""
                            break

                        if i == len(word) - 1:
                            inicio = i
                            self.classifica(texto)
                            texto = ""
                            inicio = i + 1
                            break

    def classifica(self, word):

        if word is not "":
            if word in self.chaves:
                novoElemento = Log( word, self.tipoDeClassificadores[0], self.linhaCont)
                self.log.append(novoElemento)
            elif word.isdigit():
                novoElemento = Log( word, self.tipoDeClassificadores[4], self.linhaCont)
                self.log.append(novoElemento)
            elif word in self.delimitadores:
                novoElemento = Log( word, self.tipoDeClassificadores[2], self.linhaCont)
                self.log.append(novoElemento)
            elif word in self.atribuicao:
                novoElemento = Log( word, self.tipoDeClassificadores[3], self.linhaCont)
                self.log.append(novoElemento)
            elif word in self.aditivos:
                novoElemento = Log( word, self.tipoDeClassificadores[5], self.linhaCont)
                self.log.append(novoElemento)
            elif word in self.multiplicativos:
                novoElemento = Log( word, self.tipoDeClassificadores[6], self.linhaCont)
                self.log.append(novoElemento)
            elif word in self.relacionais:
                novoElemento = Log( word, self.tipoDeClassificadores[7], self.linhaCont)
                self.log.append(novoElemento)
            elif self.isFloat(word):
                novoElemento = Log( word, self.tipoDeClassificadores[8], self.linhaCont)
                self.log.append(novoElemento)
            else:
                novoElemento = Log( word, self.tipoDeClassificadores[1], self.linhaCont)
                self.log.append(novoElemento)


# TO DO
# -> Ajeitar o número da linha que está sendo lida.
