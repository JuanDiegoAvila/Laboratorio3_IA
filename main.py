from reader import Reader 
from modelo import Modelo
from sklearn.metrics import accuracy_score

reader = Reader('./entrenamiento.txt')

modelo = Modelo(reader.training)

valores = []
for key in ["spam", "ham"]:
    for frase in reader.testing[key]:
        if key == "ham":
            valores.append(1)
        else:
            valores.append(0)

solutions = modelo.predict(reader.testing)

print(accuracy_score(valores, solutions))
