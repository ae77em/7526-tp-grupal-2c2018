# RESPUESTA 7 paso 2
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from funciones import gcl_uniforme
import constante

x_n = constante.SEMILLA
u = []  
v = []  
w = []
k = 0

for i in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    
    if (k % 3 == 0):
        u.append(x_n)
        k = 0
    if (k % 2 == 0):
        v.append(x_n)
        k = k+1
    else:
        w.append(x_n)
        k = k+1

trace = go.Scatter3d(
    x=u, y=v, z=w,
    marker=dict(
        size=1,
        color="#4faab4",
        colorscale='Viridis',
    ),
    line=dict(
        color='#1f77b4',
        width=1
    )
)

data = [trace]

layout = dict(
    width=800,
    height=700,
    autosize=False,
    title='Test espectral 3D de GCL',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        camera=dict(
            up=dict(
                x=0,
                y=0,
                z=1
            ),
            eye=dict(
                x=-1.7428,
                y=1.0707,
                z=0.7100,
            )
        ),
        aspectratio=dict(x=1, y=1, z=0.7),
        aspectmode='manual',        
    ),
)

fig = dict(data=data, layout=layout)

py.plot(fig, filename='test-espectral-3d-gcl', height=700)
