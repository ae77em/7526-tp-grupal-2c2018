# RESPUESTA 3 version 2
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

from math import log
from scipy import stats
from scipy.interpolate import interp1d

from funciones import gcl_uniforme
import constante
# Paso 1: Generamos muestras de la variable uniforme U
x_n = constante.SEMILLA
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa, usando interpolacion lineal, con los rangos dados en apunte
x_coords = [ 0, 0.00003, 0.00135, 0.00621, 0.02275, 0.06681, 0.11507, 0.15866, 0.21186, 0.27425, 0.34458, 0.42074, 0.5, 0.57926, 0.65542, 0.72575, 0.78814, 0.84134, 0.88493, 0.93319, 0.97725, 0.99379, 0.99865, 0.99997, 1]
y_coords = [-5,      -4,      -3,    -2.5,      -2,    -1.5,    -1.2,      -1,    -0.8,    -0.6,    -0.4,    -0.2,   0,     0.2,     0.4,     0.6,     0.8,       1,     1.2,     1.5,       2,     2.5,       3,       4, 5]

f_inversa = interp1d(x_coords, y_coords)

x = f_inversa(u)  # Transformacion inversa

# Mostramos histograma del resultado
data = [go.Histogram(x=x)]
py.plot(data, filename='histograma-inversa-normal-v2')

# Mostramos meida, varianza y moda muestrales y teoricos
media = np.mean(x)
varianza = np.var(x)
moda = stats.mode(x).mode[0] # tengo un solo array, i.e. una sola moda

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(0, 1, 0))

