class Modelo():

    ham = []
    spam = []
    bagHam = []
    bagSpam = []
    probabilities = {"ham": None, "spam": None}
    probabilidad_spam = 0
    probabilidad_ham = 0
    

    def __init__(self, training):
        self.training = training
        self.separateProbabilities()
        
    
    # crea una bolsa de palabras con los elementos de la lista de entrenamiento
    def getBagOfWords(self, list):
        bag = []
        for i in list:
            words = i.split(" ")
            for j in words:
                if j != '':
                    bag.append(j)
        return bag

    # separa los mensajes de entrenamiento en ham y spam
    def separateProbabilities(self):
        self.ham = self.training["ham"]
        self.spam = self.training["spam"]

        self.bagHam = self.getBagOfWords(self.ham)
        self.bagSpam = self.getBagOfWords(self.spam)

        self.spam_length = len(self.bagSpam)
        self.ham_length = len(self.bagHam)

        self.getProbabilities("ham", self.bagHam, self.ham_length)
        self.getProbabilities("spam", self.bagSpam, self.spam_length)

        self.total = dict(list(self.probabilities["spam"].items()) + list(self.probabilities["ham"].items()))
        
        palabras = []
        for i in self.total:
            if i not in palabras and i != '':
                palabras.append(i)
        self.diferentes = len(palabras)

    
    # crea un diccionario con los conteos de cada palabra
    def getProbabilities(self, type, bag, size):
        self.probabilities[type] = {}
        for i in bag:
            if i in self.probabilities[type]:
                self.probabilities[type][i] += 1
            else:
                self.probabilities[type][i] = 1
        # for i in self.probabilities[type]:
        #     self.probabilities[type][i] = self.probabilities[type][i] / size


    def getElementLenght(self, element):
        count = 0
        for i in element:
            for word in i.split(" "):
                count += 1
        return count

    # calcula la probabilidad de que un mensaje sea spam o ham        
    def naiveBayes(self, frase):
        self.probabilidad_spam = (len(self.spam) + 1) / ((len(self.spam) + len(self.ham))+1*2)
        self.probabilidad_ham = (len(self.ham) + 1) / ((len(self.spam) + len(self.ham))+1*2)

        words = frase.split(" ")
        spam_condicional = 1
        ham_condicional = 1

        for i in words:
            get_spam = self.probabilities["spam"].get(i,0)
            get_ham = self.probabilities["ham"].get(i,0)

            spam_condicional *= ((get_spam + 1) / (self.spam_length + (1 * self.diferentes)))
            ham_condicional *= ((get_ham + 1) / (self.ham_length + (1 * self.diferentes)))

        nspam_condicional = spam_condicional / (spam_condicional + ham_condicional)
        nham_condicional = ham_condicional / (spam_condicional + ham_condicional)

        p_spam = self.probabilidad_spam * nspam_condicional
        p_ham = self.probabilidad_ham * nham_condicional

        if p_spam + p_ham == 0:
            return 0
        else:
            return (p_spam / (p_spam + p_ham))
    
    def getWordCount(self, bag, word):
        count = 0
        for i in bag:
            if i == word:
                count += 1
        return count

    def predict(self, testing):
        solutions = []
        for key in ["spam", "ham"]:
            testing[key]
            for frase in testing[key]:
                prob = self.naiveBayes(frase)
                if prob > 0.5:
                    #0 = spam; 1 = ham
                    solutions.append(0)
                else:
                    solutions.append(1)
        return solutions
    




            

    
        

