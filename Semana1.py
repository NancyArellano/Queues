""" Diapositiva uno de Virtamo. Lineas de espera y teoría de colas 2016.
Agosto 2016. Try1.

Estoy asumiendo que dado un experimento, un conjunto de outcomes es un evento.
El espacio muestral es el conjunto de todos los posibles outcomes del
experimento.
Cada outcome tiene una probabilidad asociada. La probabilidad del espacio
muestral es 1.
"""

e1={1:0.0,2:0.0,3:0.0}
e2={3:0.0,4:0.0,5:0.0}
e3={5:0.0,6:0.0,7:0.0}
e4={}

S=[e1,e2,e3,e4]
print(S)

def emptiness(event):#el evento es un dict
    if len(event)==0:
        print ("Empty event")
    else:
        print("Not empty set. Length is",len(event))

def uniones(eventos):#Una lista de eventos a unir
    unes={}
    for i in eventos:
        #print(i.keys())
        unes=dict(list(unes.items())+ list(i.items()))
    print(unes.keys())

emptiness(e1)
uniones([e1,e2,e3])
