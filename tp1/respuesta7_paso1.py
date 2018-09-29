import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

def generador_congruencial_lineal(x_n):
   m = 232                     # modulus
   a = 1013904223              # multiplier
   c = 1664525                 # increment

   x = ((a * x_n) + c) % m

   return x

x_n = (90697 + 89563) // 2
u = []  # array de cantidad
v = []  # array de nro generado

for i in range(100):
   x_n = generador_congruencial_lineal(x_n)
   
   u.append( i ) 
   v.append( x_n ) 
   
   print i
   print x_n

trace = go.Scatter(
    x = u,
    y = v,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.plot(data, filename='basic-scatter')
