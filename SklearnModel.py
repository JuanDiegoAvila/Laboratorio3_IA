from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

class SklearnModel():
    def __init__(self, reader):
        self.training = reader.library[0]
        self.testing = reader.library[1]
        self.target_training = reader.library[2]
        self.target_testing = reader.library[3]
        
        self.accuracy = self.train()
        # self.model = MultinomialNB()

    def train(self):
        vectorizer = CountVectorizer(ngram_range=(1,2)).fit(self.training)
        training_vectorized = vectorizer.transform(self.training)

        model = MultinomialNB(alpha=0.1)
        model.fit(training_vectorized, self.target_training)
        predictions = model.predict(vectorizer.transform(self.testing))
        predictions2 = model.predict(vectorizer.transform(self.training))
        return [accuracy_score(self.target_testing, predictions), accuracy_score(self.target_training, predictions2)]