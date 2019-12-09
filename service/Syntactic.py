from Semantic import *

class Syntactic:
    logFinal = []
    pos = 0
    x = 0
    tipos = ["integer", "real", "boolean"]
    pilha = pilhaSemantica()
    tiposVariaveis = pilhaTipos()

    def __init__(self, log):
        self.logFinal = log

    def proximo(self):
        self.pos += 1

    def programa(self):
        if len(self.logFinal) > 0:
            
            ## Analisa se o programa inicia com a palavra reservada PROGRAM.
            if self.logFinal[self.pos].token != 'program':
                print("FALTA PROGRAM|linha: ", self.logFinal[self.pos].linha)
                return False
            #self.pilha.adicionarSimbolo(simbolo('$', '$'))
            self.proximo()

            ## Analisa se o apresenta o identificador do programa.
            if self.logFinal[self.pos].classif != "Identificador":
                print("FALTA IDENTIFICADOR DO PROGRAMA |linha: ", self.logFinal[self.pos].linha)
                return False
            self.proximo()

            ## Analisa o a presença do ; na declaração do programa.
            if self.logFinal[self.pos].token != ";":
                print("FALTA ; NA DECLARAÇÃO DO PROGRAMA |linha: ", self.logFinal[self.pos].linha)
                return False
            self.proximo()

            ## Analisa a declaração das variaveis.
            if self.logFinal[self.pos].token == "var":
                self.proximo()
                if not self.variaveis():
                    print("ERRO NA DECLARACAO DAS VARIÁVEIS |linha: ", self.logFinal[self.pos].linha)
                    return False

            ## Analisa os subprogramas.
            if self.logFinal[self.pos].token == "procedure":
                if not self.subprograma():
                    print("ERRO NA DECLARACAO DE SUBPROGRAMA |linha: ", self.logFinal[self.pos - 1].linha)
                    return False

            ## Analisa os comandos
            if self.logFinal[self.pos].token == "begin":
                
                ## SEMANTIC
                self.pilha.inicioEscopo()
                
                self.proximo()
                if not self.comandoComposto():
                    print("ERRO NA DECLARACAO DE COMMANDO COMPOSTO |linha: ", self.logFinal[self.pos].linha)
                    return False

            ## SEMANTIC
            self.pilha.fimEscopo()

            ## Analisa o fim do programa
            if self.logFinal[self.pos].token != ".":
                print("AUSENCIA DO . PARA FIM DO PROGRAMA |linha: ", self.logFinal[self.pos].linha)
                return False

        return True

    def variaveis(self):

        while self.logFinal[self.pos].classif == "Identificador":
            ## SEMANTIC
            listaDeVariaveis = []
            listaDeVariaveis.append(self.logFinal[self.pos].token)
            
            self.proximo()

            while self.logFinal[self.pos].token != ":":
                if self.logFinal[self.pos].token != ",":
                    print("FALTA , DEPOIS DE UM ID |linha: ", self.logFinal[self.pos].linha)
                    return False
                self.proximo()

                if self.logFinal[self.pos].classif != "Identificador":
                    print("FALTA ID DEPOIS DE UMA , |linha: ", self.logFinal[self.pos].linha)
                    return False
                
                ## SEMANTIC
                listaDeVariaveis.append(self.logFinal[self.pos].token)
                self.proximo()

            if self.logFinal[self.pos].token != ':':
                print("ERRO! ESPERADO UM :|linha: ", self.logFinal[self.pos].linha)
                return False
            self.proximo()

            if self.logFinal[self.pos].token not in self.tipos:
                print("TIPO DE VARIAVEL ESPERADO|linha: ", self.logFinal[self.pos].linha)
                return False

            ## SEMANTIC ##
            tipoVariaveis = ''
            if self.logFinal[self.pos].token == "integer":
                tipoVariaveis = "Inteiro"
            if self.logFinal[self.pos].token == "real":
                tipoVariaveis = "Real"

            for x in listaDeVariaveis:
                self.pilha.adicionarSimbolo( simbolo(x, tipoVariaveis) )
            ## SEMANTIC ##

            self.proximo()

            if self.logFinal[self.pos].token != ";":
                print("ERRO! ESPERADO UM ;|linha: ", self.logFinal[self.pos].linha)
                return False
            self.proximo()

        return True

    def argumentos(self):
        ## Analisa a presença do '(' no inicio da declaração dos argumentos. 
        if self.logFinal[self.pos].token != "(":
            return True

        self.proximo()

        #Analisar a declaração dos argumentos.
        while self.logFinal[self.pos].token == "var" or self.logFinal[self.pos].classif == "Identificador":
            ## SEMANTIC
            listaDeVariaveis = []

            if self.logFinal[self.pos].token == "var":
                self.proximo()

            if self.logFinal[self.pos].classif != "Identificador":
                print("FALTA ID DE ARGUMENTO |linha: ", self.logFinal[self.pos].linha)
                return False

            ## SEMANTIC
            listaDeVariaveis.append(self.logFinal[self.pos].token)

            self.proximo()

            while self.logFinal[self.pos].token != ":":
                if self.logFinal[self.pos].token != ",":
                    print("FALTA , DEPOIS DE UM ID |linha: ", self.logFinal[self.pos].linha)
                    return False

                self.proximo()

                if self.logFinal[self.pos].classif != "Identificador":
                    print("FALTA ID DEPOIS DE UMA , |linha: ", self.logFinal[self.pos].linha)
                    return False

                ## SEMANTIC
                listaDeVariaveis.append(self.logFinal[self.pos].token)
                
                self.proximo()

            if self.logFinal[self.pos].token != ':':
                print("ERRO! ESPERADO UM :|linha: ", self.logFinal[self.pos].linha)
                return False

            self.proximo()

            if self.logFinal[self.pos].token not in self.tipos:
                print("TIPO DE VARIAVEL ESPERADO|linha: ", self.logFinal[self.pos].linha)
                return False

            ## SEMANTIC
            for x in listaDeVariaveis:
                self.pilha.adicionarSimbolo(simbolo(x, self.logFinal[self.pos].token))

            self.proximo()

            if self.logFinal[self.pos].token != ";":
                if self.logFinal[self.pos].token != ")":
                    print("ERRO! ESPERADO UM ; OU ) |linha: ", self.logFinal[self.pos].linha)
                    return False
            else:
                self.proximo()


        if self.logFinal[self.pos].token != ")":
            print("ERRO! ESPERADO UM ) |linha:", self.logFinal[self.pos].linha)
            return False

        self.proximo()

        if self.logFinal[self.pos].token != ";":
            print("ERRO! ESPERADO UM ; |linha: ", self.logFinal[self.pos].linha)
            return False

        self.proximo()
        return True

    def comandos_opcionais(self):
        if not self.logFinal[self.pos].token == 'end':
            self.lista_de_comandos1()
        self.pilha.fimEscopo()

    def lista_de_comandos1(self):
        if self.comando():
            return self.lista_de_comandos2()
        else:
            return False

    def lista_de_comandos2(self):
        if self.logFinal[self.pos].token != ';':
            return True
        else:
            ## SEMANTIC
            if not self.tiposVariaveis.finalizar():
                print("Conversão inválida de Real para Integer | Linha:", self.logFinal[self.pos].linha)
                exit(-3)
            ## SEMANTIC

            self.proximo()
            if self.comando():
                return self.lista_de_comandos2()
            return True # para validar o end.#

    ## Trata o "else", ou seja, o final da condição.
    def parte_else(self):
        if self.logFinal[self.pos].token != "else":
            return True
        else:
            self.proximo()
            return self.comando()

    def comando(self):
        if self.logFinal[self.pos].classif == "Identificador":
            ## SEMANTIC
            if self.pilha.pesquisaSimbolo(self.logFinal[self.pos].token) is None:
                print("Variável não declarada:", self.logFinal[self.pos].token)
                exit(-2)
            ## SEMANTIC

            ## tratar atribuição.
            if self.logFinal[self.pos + 1].token == ':=':
                ## SEMANTIC
                self.tiposVariaveis.inicializar(self.pilha.pesquisaSimbolo(self.logFinal[self.pos].token).tipo)
                self.proximo()
                self.proximo()
                return self.expressao()
            elif self.logFinal[self.pos + 1].token == '(':
                self.proximo()
                self.proximo()
                if not self.lista_de_expressoes1():
                    return False
                if self.logFinal[self.pos].token == ')':
                    self.proximo()
                    return True
            else:
                self.tiposVariaveis.adicionarTipo(self.pilha.pesquisaSimbolo(self.logFinal[self.pos].token).tipo)
                self.proximo()
                return True

        elif self.logFinal[self.pos].token == "begin":
            if not self.tiposVariaveis.finalizar():
                print("Conversão inválida de Real para Integer | Linha:", self.logFinal[self.pos].linha)
                exit(-3)
            self.pilha.inicioEscopo()
            self.proximo()
            return self.comandoComposto()

        ## tratando a condicional if.
        elif self.logFinal[self.pos].token == "if":
            self.proximo()
            if not self.expressao():
                return False
            if self.logFinal[self.pos].token != "then":
                return False
            self.proximo()
            if not self.comando():
                return False
            return self.parte_else()

        ## tratando a condicional while.
        elif self.logFinal[self.pos].token == "while":
            self.proximo()
            if not self.expressao():
                return False
            if self.logFinal[self.pos].token != "do":
                return False
            self.proximo()
            if not self.comando():
                return False
            return True
        else:
            return False

    def lista_de_expressoes1(self):
        if self.expressao():
            return self.lista_de_expressoes2()
        else:
            return False

    def lista_de_expressoes2(self):
        if self.logFinal[self.pos].token == ',':
            self.proximo()
            if not self.expressao():
                return False
            return self.lista_de_expressoes2()
        else:
            return True

    ## Analisa expressões simples e relacional:. exemplo: (var1 + var2) > (var3).
    def expressao(self):
        if self.expressao_simples1():
            if self.op_relacional():
                if not self.expressao_simples1():
                    print("ERRO DE EXPRESSAO", self.logFinal[self.pos].linha)
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False

    def expressao_simples1(self):
        if self.termo1():
            return self.expressao_simples2()
        elif self.sinal():
            if self.termo1():
                return self.expressao_simples2()
            else:
                return False

    def expressao_simples2(self):
        if self.op_aditivo():
            if not self.termo1():
                return False
            else:
                return self.expressao_simples2()
        else:
            return True

    def termo1(self):
        if self.fator():
            return self.termo2()
        else:
            return False

    ## Analisa temos com operadores multiplicativos.
    def termo2(self):
        if not self.op_multiplicativo():
            return True
        else:
            if not self.fator():
                print("fator()")
                return False
            if not self.termo2():
                print("termo2")
                return False
            print("cheguei aqui")
            return True

    def fator(self):
        if self.logFinal[self.pos].classif == "Identificador":
            print("Identificador", self.logFinal[self.pos].classif)
            ## SEMANTIC
            if self.pilha.pesquisaSimbolo(self.logFinal[self.pos].token) == None:
                print("Variável não declarada:", self.logFinal[self.pos].token)
                exit(-2)
            self.tiposVariaveis.adicionarTipo(self.pilha.pesquisaSimbolo(self.logFinal[self.pos].token).tipo)
            ## SEMANTIC

            self.proximo()
            if self.logFinal[self.pos].token == '(':
                self.proximo()
                if not self.lista_de_expressoes1():
                    return False
                self.proximo()
                if not self.logFinal[self.pos].token == ')':
                    return False
                return True
            else:
                return True

        ## Analisa a ocorrência de uma nova expressão.
        elif self.logFinal[self.pos].token == '(':
            self.proximo()
            if not self.expressao():
                return False
            if self.logFinal[self.pos].token == ')':
                self.proximo()
            else:
                return False
            return True

        ## Analisar os números.
        elif self.logFinal[self.pos].classif in ["Real", "Inteiro"]:
            print("entrei", self.logFinal[self.pos].classif)
            ## SEMANTIC
            self.tiposVariaveis.adicionarTipo(self.logFinal[self.pos].classif)
            self.proximo()
            return True

        elif self.logFinal[self.pos].classif == "Palavra Reservada": ## Chave
            if self.logFinal[self.pos].token in ["true", "false"]:
                self.proximo()
                return True
            elif self.logFinal[self.pos].token == "not":
                self.proximo()
                return self.fator()

    ## Analisa sinal.
    def sinal(self):
        if self.logFinal[self.pos] in ['+', '-']:
            self.proximo()
            return True
        else:
            return False

    ## Analisa operadores relacionais.
    def op_relacional(self):
        if self.logFinal[self.pos].token in ["=", "<", ">", "<=", ">=", "<>"]:
            self.proximo()
            return True
        else:
            return False

    ## Analisa operadores Aditivos.
    def op_aditivo(self):
        if self.logFinal[self.pos].token in ["+", "-", "or"]:
            self.proximo()
            return True
        else:
            return False

    ## Analisa operadores multiplicativos.
    def op_multiplicativo(self):
        if self.logFinal[self.pos].token in ["*", "/", "and"]:
            self.proximo()
            return True
        else:
            return False

    ## Analisa os comandos dentro do escopo.
    def comandoComposto(self):
        if self.logFinal[self.pos].token == "end":
            ## SEMANTIC
            self.pilha.fimEscopo()
            self.proximo()
            return True
        else:
            if not self.lista_de_comandos1():
                return False
            else:
                ## validar a existência do 'end' ao final do subprograma.
                if self.logFinal[self.pos].token != "end":
                    print("AUSENCIA DO END |linha: ", self.logFinal[self.pos].linha)
                    return False
                else:
                    ## SEMANTIC
                    if not self.tiposVariaveis.finalizar():
                        print("Conversão inválida de Real para Integer | Linha:", self.logFinal[self.pos].linha )
                        exit(-3)
                    self.pilha.fimEscopo()
                    ## SEMANTIC
                    self.proximo()
                    return True

    def subprograma(self):

        while self.logFinal[self.pos].token == "procedure":

            self.proximo()

            if self.logFinal[self.pos].classif != "Identificador":
                print("FALTA ID DEPOIS DE UMA , |linha:", self.logFinal[self.pos].linha)
                return False

            ## SEMANTIC
            if self.pilha.pesquisaSimbolo(self.logFinal[self.pos].token) != None:
                print("Multiplas funções com o mesmo nome:", self.logFinal[self.pos].token)
                exit(-2)
            self.pilha.adicionarSimbolo(simbolo(self.logFinal[self.pos].token, "Procedure"))
            self.pilha.adicionarSimbolo(simbolo('$', '$'))
            ## SEMANTIC

            self.proximo()

            ## Analisa a declaração dos argumentos do subprograma.
            if not self.argumentos():
                print("ERRO NA DECLARACAO DE ARGUMENTOS DE SUBPROGRAMA |linha: ", self.logFinal[self.pos].linha)
                return False

            ## Analisa as variaveis do subprograma.
            if self.logFinal[self.pos].token == "var":
                self.proximo()
                if not self.variaveis():
                    print("ERRO NA DECLARACAO DAS VARIÁVEIS DE SUBPROGRAMA |linha: ", self.logFinal[self.pos].linha)
                    return False

            ## Analisa um novo subprograma.
            if self.logFinal[self.pos].token == "procedure":
                ## SEMANTIC
                self.pilha.adicionarSimbolo(simbolo(self.logFinal[self.pos].token, "Procedure"))
                self.pilha.adicionarSimbolo(simbolo('$', '$'))
                ## SEMANTIC
                if not self.subprograma():
                    print("ERRO NA DECLARACAO DE SUBPROGRAMA DE SUBPROGRAMA |linha: ", self.logFinal[self.pos - 1].linha)
                    return False

            ## Analisa o escopo.
            if self.logFinal[self.pos].token == "begin":
                ## SEMANTIC
                self.pilha.inicioEscopo()
                self.proximo()
                if not self.comandoComposto():
                    print("ERRO NA DECLARACAO DE COMMANDO COMPOSTO |linha: ", self.logFinal[self.pos].linha)
                    return False

            ## Analisa a existencia do ';' no final do subprograma.
            if self.logFinal[self.pos].token != ";":
                print("ERRO! ESPERADO UM ;|linha:", self.logFinal[self.pos - 1].linha)
                return False
            self.proximo()

        ## SEMANTIC
        self.pilha.fimEscopo()
        return True
