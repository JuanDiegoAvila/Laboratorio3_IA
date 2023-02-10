import re
import unicodedata

class Reader():

    dictionary = {"ham": [], "spam": []}

    def __init__(self, path):
        self.path = path
        self.readlines()

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
        

        
