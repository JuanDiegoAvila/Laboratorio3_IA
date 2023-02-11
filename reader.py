import re
import unicodedata
from sklearn.model_selection import train_test_split

class Reader():


    def __init__(self, path):
        self.dictionary = {"ham": [], "spam": []}
        self.completo = []
        self.training = {"ham": [], "spam": []}
        self.validation = {"ham": [], "spam": []}
        self.testing = {"ham": [], "spam": []}
        self.path = path
        self.readlines()
        self.separacion()

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def readlines(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                name = line.split("\t")[0]
                value = self.clean(line.replace("\n", "").split("\t")[1])
                self.dictionary[name].append(value)
        
    def clean(self, text):
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
        new = re.sub(r'[^A-Za-z\s]+', '', text.lower())
        return new
        
    def separacion(self):
        self.completo = self.dictionary["ham"] + self.dictionary["spam"]
        text = []
        target = []
        for i in self.completo:
            text.append(i)
            if i in self.dictionary["ham"]:
                target.append(1)
            else:
                target.append(0)

        training, testing, target_training, target_testing = train_test_split(text, target, test_size=0.3, random_state=1234)

        self.library = [training, testing, target_training, target_testing]

        self.training["ham"] = [training[i] for i in range(0, len(training)) if target_training[i] == 1]
        self.training["spam"] = [training[i] for i in range(0, len(training)) if target_training[i] == 0]

        self.testing["ham"] = [testing[i] for i in range(0, len(testing)) if target_testing[i] == 1]
        self.testing["spam"] = [testing[i] for i in range(0, len(testing)) if target_testing[i] == 0]

