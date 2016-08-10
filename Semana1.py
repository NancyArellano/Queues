""" Diapositiva uno de Virtamo. Lineas de espera y teoría de colas 2016.
Agosto 2016. Try1.

Estoy asumiendo que dado un experimento, un conjunto de outcomes es un evento.
El espacio muestral es el conjunto de todos los posibles outcomes del
experimento.
Cada outcome tiene una probabilidad asociada. La probabilidad del espacio
muestral es 1.
"""
import random

class Evento(dict):
    def __init__(self, name=None, proba=None):
        self.name=name
        self.proba=proba

    def creacion(self):
        items=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        probas=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        out=random.sample(items,3)
        prob=random.sample(probas,3)

        for i in out:
            #print (i)
            self.name=i
        for j in prob:
            #print(j)
            self.probas=j
        #print(len(probas))
        return self

e=Evento()
e.creacion()
for i in e:
    print (i.keys())
    print(i.proba)

#out=[]
#items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#out=random.sample(items,3)
#print (out)
