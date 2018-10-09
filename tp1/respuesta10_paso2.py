# RESPUESTA 10 paso 2
import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp
from math import sqrt

import numpy as np
import scipy.stats as st

from funciones import funcionH
from funciones import generador_aceptacion_rechazon_variable_normal
import constante


muestra = []  # array de normales
x = []  # array de normales
yEmpirica = []  # array de normales
yReal = []  # array de normales

funcionDistribucionNormal = st.norm(35, 25)
cantidadMuestras = constante.CANT_EXPERIMENTOS

for _ in range(cantidadMuestras):
    x_n = generador_aceptacion_rechazon_variable_normal()
    muestra.append(x_n)

muestra.sort()

for indice, unaMuestra in enumerate(muestra, start=1):
    if unaMuestra < 0:
        print unaMuestra
    x.append(unaMuestra)
    yEmpirica.append(indice/float(cantidadMuestras))
    yReal.append(funcionDistribucionNormal.cdf(unaMuestra))

trace0 = go.Scatter(
    x=x,
    y=yEmpirica,
    mode='lines+markers',
    name='empirica'
)
trace1 = go.Scatter(
    x=x,
    y=yReal,
    mode='lines+markers',
    name='real'
)

data = [trace0, trace1]

py.plot(data, filename='normal empirica vs real')
