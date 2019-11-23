class Log:

    def __init__(self):
        self.token = []
        self.classif = []
        self.linha = []

    def printLog(self):
        print("| Token            | Classificação         | Linha")
        print("|------------------|-----------------------|------")

        for i in range(len(self.token)):
            print("|", self.token[i], "-" * (15 - len(self.token[i])), "|", self.classif[i], "-" * (20 - len(self.classif[i])), "|", self.linha[i])

    
    def addLog(self, token, classif, line):
        self.token.append(token)
        self.classif.append(classif)
        self.linha.append(line)