class Log:

    def __init__(self, token, classif, linha):
        self.token = token
        self.classif = classif
        self.linha = linha

    def printLog(self, log):
        print("| Token            | Classificação         | Linha")
        print("|------------------|-----------------------|------")
        
        for i in range(len(log)):
            print("|", log[i].token, "-" * (15 - len(log[i].token)), "|", log[i].classif, "-" * (20 - len(log[i].classif)), "|", log[i].linha)

    
    def addLog(self, token, classif, line):
        self.token.append(token)
        self.classif.append(classif)
        self.linha.append(line)