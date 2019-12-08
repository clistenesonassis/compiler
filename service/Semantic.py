class simbolo:
    simbolo = ''
    tipo = ''

    def __init__(self, simb, tip):
        self.simbolo = simb
        self.tipo = tip


class pilhaSemantica:
    dados = []  # type: List(simbolo)
    begin = 0

    def inicioEscopo(self):
        self.begin += 1
        #print(self.begin)

    def fimEscopo(self):
        if self.begin > 0:
            self.begin -= 1
            #print(self.begin)
        else:
            self.limparEscopo()
            #print("-$")

    def adicionarSimbolo(self, simb):
        if simb.simbolo != '$':
            if self.pesquisaSimboloEscopo(simb.simbolo) != None:
                print("Multiplas variaveis com o mesmo identificador no mesmo escopo")
                exit(-1)
        if simb.tipo == "integer":
            simb.tipo = "Inteiro"
        #print(simb.simbolo, simb.tipo)
        self.dados.append(simb)

    def pesquisaSimbolo(self, simb):
        for x in reversed(self.dados):
            if x.simbolo == simb:
                return x
        return None

    def pesquisaSimboloEscopo(self, simb):
        for x in reversed(self.dados):
            if x.simbolo == '$':
                return None
            if x.simbolo == simb:
                return x
        return None

    def limparEscopo(self):
        x = simbolo('', '')
        while x.simbolo != '$':
            x = self.dados.pop()


class pilhaTipos:
    receptor = ''
    argumento = ''

    def inicializar(self, tipo):
        if self.receptor != '':
            if self.argumento == '':
                self.receptor = ''
                self.argumento = ''
                self.operacao = False
        self.receptor = tipo
        print(self.receptor, ":=")

    def operacao(self):
        self.operacao = True

    def adicionarTipo(self, tipo):
        if tipo == "integer":
            tipo = "Inteiro"
        if tipo == "real":
            tipo = "Real"
        if self.argumento != '':
            if tipo != self.argumento:
                self.argumento = "Real"
        else:
            self.argumento = tipo
        print(self.argumento)

    def finalizar(self):
        print(self.receptor, ":=", self.argumento)
        print("----------------------")
        if self.receptor != '':
            if self.argumento == '':
                self.receptor = ''
                self.argumento = ''
                return True
            if self.receptor == "Inteiro" and self.argumento == "Real":
                return False
            self.receptor = ''
            self.argumento = ''
            return True
        else:
            self.receptor = ''
            self.argumento = ''
            return True