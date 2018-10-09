# RESPUESTA 2
import numpy as np
from scipy import stats
from math import log

import plotly.plotly as py
import plotly.graph_objs as go

from funciones import gcl_uniforme
import constante

# Paso 1: Generamos muestras de la variable uniforme U
x_n = constante.SEMILLA
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa
paramLambda = float(1)/float(15)
for i in range(len(u)):
    x.append(-log(1-u[i])/paramLambda)  # Transformacion inversa

# Mostramos histograma del resultado
data = [go.Histogram(x=x)]
py.plot(data, filename='histograma-inversa-exponencial')

# Mostramos meida, varianza y moda muestrales y teoricos
media = np.mean(x)
varianza = np.var(x)
moda = stats.mode(x).mode[0]  # tengo un solo array, i.e. una sola moda

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(
    media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(
    15, 15*15, 0))
