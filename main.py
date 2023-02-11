from reader import Reader 
from modelo import Modelo
from rendimiento import Metrica
from SklearnModel import SklearnModel

reader = Reader('./entrenamiento.txt')

modelo = Modelo(reader.training)

solutions = modelo.predict(reader.testing)
metrica = Metrica(reader.testing, solutions)

solutions2 = modelo.predict(reader.training)
metrica2 = Metrica(reader.training, solutions2)

print('\nMetrica de desempeno de testing ->',metrica.accuracy)
print('\nMetrica de desempeno de training ->', metrica2.accuracy)

other_model = SklearnModel(reader)
print('\nMetrica de desempeno de testing utilizando libreria ->', other_model.accuracy[0])
print('\nMetrica de desempeno de training utilizando libreria ->', other_model.accuracy[1])

salir = False
while not salir:

    frase = input('\n\nIngrese una frase para clasificarlo como spam o ham -> ')

    cleaned_frase = reader.clean(frase)
    response = modelo.predictFrase(cleaned_frase)

    print('\n\tLa probabilidad de spam es -> ', response[1])
    print('\tLa probabilidad de ham es -> ', response[2])

    if response[0] == 0:
        print('\n\t--------- La frase es spam ---------')
    else:
        print('\n\t--------- La frase es ham ---------')

    salir = input('\nDesea ingresar otra frase? (s/n) -> ') == 'n'

# ¿Cuál implementación lo hizo mejor? ¿Su implementación o la de la librería?
# ¿Por qué cree que se debe esta diferencia?

# La implementación de la librería lo hizo mejor en ambos casos.
# Esto se debe a que las librerías ya tienen implementados algoritmos que son más eficientes que los que nosotros implementamos.
# Estas librerías tambien son desarrolladas por expertos en el tema. Ademas estas librerías son sometidas a diferentes pruebas 
# y documentaciones antes de su lanzamiento. Cosa que nuestra implementación no tiene.