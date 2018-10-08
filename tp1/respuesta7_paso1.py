import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from funciones import generador_congruencial_lineal
import constante

x_n = constante.SEMILLA
u = []
v = []  

for i in range(constante.CANT_EXPERIMENTOS):
    x_n = generador_congruencial_lineal(x_n)
    
    if (i % 2 == 0):
        u.append(x_n)
    else:
        v.append(x_n)

trace = go.Scatter(
    x=u,
    y=v,
    mode='markers',
    marker=dict(
        size=3,
        color="#4faab4",
        colorscale='Viridis',
    ),
)

data = [trace]

py.plot(data, filename='test-espectral-2d-gcl')
