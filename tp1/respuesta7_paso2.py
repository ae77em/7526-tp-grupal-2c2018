import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

def generador_congruencial_lineal(x_n):
   m = 232                     # modulus
   a = 1013904223              # multiplier
   c = 1664525                 # increment

   x = ((a * x_n) + c) % m

   return x

x_n = (90697 + 89563) // 2
t = []  # array de cantidad
u = []  # array de cantidad
v = []  # array de nro generado

for i in range(100):
   x_n = generador_congruencial_lineal(x_n)
   
   t.append( i ) 
   u.append( i ) 
   v.append( x_n ) 
   
   print i
   print x_n


trace = go.Scatter3d(
    x=t, y=u, z=v,
    marker=dict(
        size=4,
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
    title='Iris dataset',
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
        aspectratio = dict( x=1, y=1, z=0.7 ),
        aspectmode = 'manual'
    ),
)

fig = dict(data=data, layout=layout)

py.plot(fig, filename='pandas-brownian-motion-3d', height=700)