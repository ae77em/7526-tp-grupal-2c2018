import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from generador_congruencial_lineal import generador_congruencial_lineal

x_n = (90697 + 89563) // 2
u = []  # array de cantidad
v = []  # array de nro generado

for i in range(10000):
    x_n = generador_congruencial_lineal(x_n, k=1)
    x_n2 = generador_congruencial_lineal(x_n, k=2)

    u.append(x_n)
    v.append(x_n2)

trace = go.Scatter(
    x=u,
    y=v,
    mode='markers'
)

data = [trace]

py.plot(data, filename='basic-scatter')
