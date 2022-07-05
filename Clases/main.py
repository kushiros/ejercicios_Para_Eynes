import math
import matplotlib.pyplot as plt
import numpy as np


class circulo():
    def __init__(self,radio):
        if radio<=0:
            raise ValueError("el radio no puede ser menor a 0")
        elif radio>0:
            self.radio = radio
    def area(self):
        area = self.radio*self.radio*math.pi
        return area
    def perimetro(self):
        perimetro = self.radio*2*math.pi
        return perimetro
    def modificarRadio(self,int):
        if int<=0:
            raise ValueError("el radio no puede ser menor a 0")
        elif int>0:
            self.radio = int
    def __str__(self):
        t = np.linspace(0,2*np.pi)
        x1 = self.radio*np.cos(t)
        y1 = self.radio*np.sin(t)

        plt.plot(x1,y1,color='blue')
        plt.scatter([0],[0],color="r")
        plt.show()
        return ("")
    def __mul__(self,other):
        self.radio = self.radio * other
        return self

while True:
    try:
        hola = circulo(int(input("ingrese un radio para el circulo: ")))
        print(f"el area del circulo es de {hola.area()}")
        print(f"el perimetro del circulo es de {hola.perimetro()}")
        print(hola)
        break
    except ValueError as radioMenorA0:
        print(radioMenorA0)
while True:
    try:
        hola.modificarRadio(int(input("ingrese un entero para modificar el radio del circulo: ")))
        print(f"el area del circulo es de {hola.area()}")
        print(f"el perimetro del circulo es de {hola.perimetro()}")
        print(hola)
        hola = hola*5
        print(hola)
        print(f"el area del circulo es de {hola.area()}")
        print(f"el perimetro del circulo es de {hola.perimetro()}")
        break
    except ValueError as radioMenorA0:
        print(radioMenorA0)
