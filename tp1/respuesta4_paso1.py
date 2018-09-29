import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp

def funcionH(unNro):
    result = (pow( unNro - 1 , 2) * 1) / 2
    
    return exp(result)

# funciones auxiliares
def generador_aceptacion_rechazon_variable_normal():
    U = 0
    count = 0
    continuar = True

    while( continuar ):
        Y = log(  random.uniform(0, 1)   ) * -1 #genero variable con distribucion exp -1

        U = random.uniform(0, 1) 

        count = count + 1

        print "intento de busqueda jajjaja"
        print count

        if U <= funcionH( Y ):
            continuar = False
            
    if U < 0.5:
        return 5*Y + 35
    else:
        return 5*Y*-1 + 35

# Paso 1: Generamos muestras de la variable uniforme U
u = []  # array de uniformes

for _ in range(100000):
    x_n = generador_aceptacion_rechazon_variable_normal()
    u.append(x_n)
    print "Variable generada"
    print x_n

# Mostramos histograma del resultado
data = [go.Histogram(x=u)]
py.plot(data, filename='histograma-inversa')
