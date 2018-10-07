import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp
from math import sqrt

import numpy as np
import scipy.stats as st

def funcionH(unNro):
    result = (pow(unNro - 1, 2) * 1) / 2

    return exp(result)

# funciones auxiliares


def generador_aceptacion_rechazon_variable_normal():
    U = 0
    count = 0
    continuar = True

    while(continuar):
        # genero variable con distribucion exp -1
        Y = log(random.uniform(0, 1)) * -1

        U = random.uniform(0, 1)

        count = count + 1

        if U <= funcionH(Y):
            continuar = False

    if U < 0.5:
        return 5*Y + 35
    else:
        return 5*Y*-1 + 35

#------------------------------------------------------

muestra = []  # array de normales
x = []  # array de normales
yEmpirica = []  # array de normales
yReal = []  # array de normales

funcionDistribucionNormal = st.norm(35, 25)
cantidadMuestras = 100000

for _ in range(cantidadMuestras):
    x_n = generador_aceptacion_rechazon_variable_normal()
    muestra.append(x_n)

muestra.sort()

for indice, unaMuestra in enumerate(muestra, start=1):
    if unaMuestra < 0:
        print unaMuestra
    x.append( unaMuestra )
    yEmpirica.append( indice/float(cantidadMuestras) )
    yReal.append( funcionDistribucionNormal.cdf( unaMuestra ) )

trace0 = go.Scatter(
    x = x,
    y = yEmpirica,
    mode = 'lines+markers',
    name = 'empirica'
)
trace1 = go.Scatter(
    x = x,
    y = yReal,
    mode = 'lines+markers',
    name = 'real'
)

data = [trace0, trace1]

py.plot(data, filename='normal empirica vs real')