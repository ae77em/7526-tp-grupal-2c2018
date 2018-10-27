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
from funciones import normal_por_aceptacion_rechazo
import constante


x = []  # array de normales
yEmpirica = []  # array de normales
yReal = []  # array de normales

funcionDistribucionNormal = st.norm(35, 5)

cantidadMuestras = constante.CANT_EXPERIMENTOS

muestra = normal_por_aceptacion_rechazo(35, 5)
muestra.sort()

for indice, unaMuestra in enumerate(muestra, start=1):
    x.append(unaMuestra)
    yEmpirica.append(indice/float(cantidadMuestras))
    yReal.append(funcionDistribucionNormal.cdf(unaMuestra))

trace0 = go.Scatter(
    x=x,
    y=yEmpirica,
    mode='lines+markers',
    name='empirica',    
    marker = dict(
          color = 'rgb(231, 99, 250, 0.5)',
          size = 0.1
        )
)
trace1 = go.Scatter(
    x=x,
    y=yReal,
    mode='lines+markers',
    name='real',
    marker = dict(
          color = 'rgba(17, 157, 255, 0.5)',
          size = 0.1
        )
)

data = [trace0, trace1]

py.plot(data, filename='test-smirnov-normal-empirica-vs-real')
