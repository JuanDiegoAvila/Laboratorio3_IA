class Metrica():
    def __init__(self, testing, solution):
        self.testing = testing
        self.solution = solution
        self.valores = self.getReales()
        self.accuracy = self.accuracy()
        
    
    def accuracy(self):
        correct = 0
        for i in range(len(self.solution)):
            if self.solution[i] == self.valores[i]:
                correct += 1

        return correct / len(self.valores)

    def getReales(self):
        # valores reales
        valores = []
        for key in ["spam", "ham"]:
            for frase in self.testing[key]:
                if key == "ham":
                    valores.append(1)
                else:
                    valores.append(0)
        return valores
        
