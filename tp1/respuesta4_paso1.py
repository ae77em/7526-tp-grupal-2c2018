import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp

import constante

def funcionH(unNro):
    result = (pow( unNro - 1 , 2) * 1) / 2
    
    return exp(result)

# funciones auxiliares
def generador_aceptacion_rechazon_variable_normal():
    U = 0
    continuar = True

    while( continuar ):
        Y = log(  random.uniform(0, 1)   ) * -1 #genero variable con distribucion exp -1

        U = random.uniform(0, 1) 

        if U <= funcionH( Y ): #si el resultado es mayor a la uniforme, la variable Y se toma, sino se rechaza
            continuar = False
            
    if U < 0.5: #por simetria de la imagen de la normal
        return 5*Y + 35
    else:
        return 5*Y*-1 + 35

u = []  # array de normales

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = generador_aceptacion_rechazon_variable_normal()
    u.append(x_n)

# Mostramos histograma del resultado
data = [go.Histogram(x=u)]
py.plot(data, filename='histograma-normal')
