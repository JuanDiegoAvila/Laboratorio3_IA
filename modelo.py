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
                bag.append(j)
        return bag

    # separa los mensajes de entrenamiento en ham y spam
    def separateProbabilities(self):
        for i in self.training:
            if i == 'ham':
                self.ham = self.training[i]
            else:
                self.spam = self.training[i]
        
        self.bagHam = self.getBagOfWords(self.ham)
        self.bagSpam = self.getBagOfWords(self.spam)
        self.getProbabilities("ham", self.bagHam)
        self.getProbabilities("spam", self.bagSpam)
    
    # crea un diccionario con las probabilidades de cada palabra
    def getProbabilities(self, type, bag):
        self.probabilities[type] = {}
        for i in bag:
            if i in self.probabilities[type]:
                self.probabilities[type][i] += 1
            else:
                self.probabilities[type][i] = 1
        for i in self.probabilities[type]:
            self.probabilities[type][i] = self.probabilities[type][i] / len(bag)

    # calcula la probabilidad de que un mensaje sea spam o ham        
    def naiveBayes(self, frase):
        self.probabilidad_spam = (len(self.spam) + 1) / ((len(self.spam) + len(self.ham))+1*2)
        self.probabilidad_ham = (len(self.ham) + 1) / ((len(self.spam) + len(self.ham))+1*2)

        total = dict(list(self.probabilities["spam"].items()) + list(self.probabilities["ham"].items()))
        palabras = []
        for i in total:
            if i not in palabras:
                palabras.append(i)
        diferentes = len(palabras)


        words = frase.split(" ")
        spam_condicional = 1
        ham_condicional = 1

        for i in words:
            get_spam = self.probabilities["spam"].get(i,0)
            get_ham = self.probabilities["ham"].get(i,0)

            spam_condicional *= ((get_spam + 1) / (len(self.bagSpam) + (1 * diferentes)))
            ham_condicional *= ((get_ham + 1) / (len(self.bagHam) + (1 * diferentes)))

        print('spam_condicional: ', spam_condicional)
        print('ham_condicional: ', ham_condicional)

        p_spam = self.probabilidad_spam * spam_condicional
        p_ham = self.probabilidad_ham * ham_condicional

        print('probabilidad_spam: ', p_spam)
        print('probabilidad_ham: ', p_ham)
        
        es_spam = p_spam / (p_spam + p_ham)
        es_ham = p_ham / (p_spam + p_ham)

        if es_spam > es_ham:
            return "spam"
        else:
            return "ham"





            

    
        

