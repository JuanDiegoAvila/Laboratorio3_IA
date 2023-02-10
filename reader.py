import re
import unicodedata
from math import floor
import random

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
        training = floor(len(self.completo) * 0.8)
        validation = floor(len(self.completo) * 0.1)
        testing = floor(len(self.completo) * 0.1)

        if training + validation + testing < len(self.completo):
            training += len(self.completo) - (training + validation + testing)

        for i in range(0, training):
            random_temp = random.randint(0, len(self.completo) - 1)
            key = "ham" if self.completo[random_temp] in self.dictionary["ham"] else "spam"
            self.training[key].append(self.completo[random_temp])
            self.completo.remove(self.completo[random_temp])

        for i in range(0, validation):
            random_temp = random.randint(0, len(self.completo) - 1)
            key = "ham" if self.completo[random_temp] in self.dictionary["ham"] else "spam"
            self.validation[key].append(self.completo[random_temp])
            self.completo.remove(self.completo[random_temp])

        for i in range(0, testing):
            random_temp = random.randint(0, len(self.completo) - 1)
            key = "ham" if self.completo[random_temp] in self.dictionary["ham"] else "spam"
            self.testing[key].append(self.completo[random_temp])
            self.completo.remove(self.completo[random_temp])

