""" Diapositiva dos de Virtamo. Lineas de espera y teoría de colas 2016.
Agosto 2016.
"""
import random
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(n-r) / f(r)

class Bernoulli:
    def __init__(self,prob):
        self.prob=prob
    def bern(self):
        r=random.uniform(0,1)
        if r>self.prob:
            r=0
        elif r<=self.prob:
            r=1
        return(r)

class BinomialFormula:#Nos da la probabilidad
    def __init__(self,n,prob,x):
        self.n=n
        self.prob=prob
        self.x=x
    def bino(self):
        pr=nCr(self.n,self.x)*(((self.prob)**self.x)*((1-self.prob) ** (self.n - self.x)))
        return pr
    def mediaBin(self):
        media=self.n*self.prob
        return media

class Binomial_SinFormula(Bernoulli):#Nos da el número de éxitos en un conjunto de n ensayos
    def __init__(self,n,prob):
        Bernoulli.__init__(self,prob)
        self.n=n
        self.prob=prob
    def binsf(self):
        exitoB=0
        for i in range(self.n):
            #BeP=Bernoulli(self.prob)
            y1=self.bern()
            if y1==1:
                exitoB=exitoB+1
        #print("exitos Binomial: ",exitoB)
        return exitoB

class BinNeg_Formula:
    def __init__(self,n,prob,k):
        self.n=n
        self.prob=prob
        self.k=k
    def bineg(self):
        pr=nCr(self.n-1,self.k-1)*(((self.prob)**self.k)*((1-self.prob) ** (self.n - self.k)))
        return pr
    def medianeg(self):
        medin=self.k/self.prob#La k es la x
        return medin

class BinNeg_SinFormula(Bernoulli):
#el numero de intentos para el k-esimo
#exito
    def __init__(self,n,prob,k):
        Bernoulli.__init__(self,prob)
        self.n=n
        self.prob=prob
        self.k=k
    def binegsf(self):
        intento=1
        exito=0
        for i in range(self.n):
            y1=self.bern()
            intento=intento+1
        #    print("intento ",intento)
            #print("Bernoulli: ",y1)
            if y1==1:
                exito=exito+1
                if exito==self.k:
                    break

        #print("exito: ",exito," "," intento :",intento)
        return intento

class Geo_Formula:
    def __init__(self,n,prob):
        self.n=n
        self.prob=prob
    def geo(self):
        pr=(self.prob)*((1-self.prob)**(self.n-1))
        return pr
    def mediageo(self):
        medin=1/(self.prob)
        return medin

class Geo_SinFormula(Bernoulli):
    def __init__(self,n,prob):
        Bernoulli.__init__(self,prob)
        self.n=n
        self.prob=prob
    def geosf(self):
        exito=0
        intento=1
        for i in range(self.n):
            y1=self.bern()
            #print(y1)
            if y1==1:
                exito=exito+1
                break
            elif y1==0:
                intento=intento+1
            #print("exito: ",exito," ","intento: ",intento)
        return intento

#############
#######
###

p=0.6
n=10000

#Bernoulli
exitos=0
fracasos=0
B=0
for i in range(n):
    B=Bernoulli(p)
    y=B.bern()
    if y==1:
        exitos=exitos+1
    elif y==0:
        fracasos=fracasos+1
probex=exitos/n
probfr=fracasos/n
print(" ")
print("Bernoulli: exitos ",probex," ","fracasos ",probfr)
print(" ")

#Binomial con fórmula.
p1=1/6
n1=51
x1=20
BI=BinomialFormula(n1,p1,x1)
print("Pob_Binomial: ",BI.bino())
print("Media_Binomial: ",BI.mediaBin())

#Binomial Sin Fórmula
mediaPrueba=0
for i in range(n):
    BSF=Binomial_SinFormula(n1,p1)
    #print("exitos: ",BSF.binsf())
    mediaPrueba=mediaPrueba+BSF.binsf()
    #print("mediaPrueba: ",mediaPrueba)
    media=mediaPrueba/n
print("Media_BinSinF: ",media)
print(" ")

#Binomial Negativa con fórmula
p2=1/6
n2=51
k2=5
BN=BinNeg_Formula(n2,p2,k2)
print("Prob_BinNeg: ",BN.bineg())
print("Media_BinNeg: ",BN.medianeg())

#Binomial Negativa sin fórmula
mediaPrueba1=0
for i in range(n):
    BNSF=BinNeg_SinFormula(n2,p2,k2)
    mediaPrueba1=mediaPrueba1+BNSF.binegsf()
    media1=mediaPrueba1/n
print("Media_BNSinF: ",media1)
print(" ")

#Geométrica Con Fórmula
n3=51
p3=1/6
Geo=Geo_Formula(n3,p3)
print("Geo_CFormula: ",Geo.geo())
print("Media_geo: ",Geo.mediageo())

#Geométrica Sin Fórmula
mediaPrueba2=0
for i in range(n):
    geos=Geo_SinFormula(n3,p3)
    mediaPrueba2=mediaPrueba2+geos.geosf()
    media2=mediaPrueba2/n
print("Media_GeoSF: ",media2)
print(" ")


    #Comentario para que me deje tener
    #el espacio blanco
