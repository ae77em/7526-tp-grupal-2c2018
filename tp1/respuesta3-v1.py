# RESPUESTA 3 version 1
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

from math import log
from scipy import stats
from scipy.interpolate import interp1d

from funciones import gcl_uniforme
import constante


def obtenerX(y, y1, y2, x1, x2):
    return x1 + (y - y1)*(x2 - x1) * (1 / (y2 - y1))


def obtenerTransfInversa(y):
    x = 0

    if(y >= 0 and y < 0.0003):
        x = obtenerX(y, 0, 0.0003, -5, -4)

    elif(y >= 0.0003 and y < 0.00135):
        x = obtenerX(y, 0.0003, 0.00135, -4, -3)

    elif(y >= 0.00135 and y < 0.00621):
        x = obtenerX(y, 0.00135, 0.00621, -3, -2.5)

    elif(y >= 0.00621 and y < 0.02275):
        x = obtenerX(y, 0.00621, 0.02275, -2.5, -2)

    elif(y >= 0.02275 and y < 0.06681):
        x = obtenerX(y, 0.02275, 0.06681, -2, -1.5)

    elif(y >= 0.06681 and y < 0.11507):
        x = obtenerX(y, 0.06681, 0.11507, -1.5, -1.2)

    elif(y >= 0.11507 and y < 0.15866):
        x = obtenerX(y, 0.11507, 0.15866, -1.2, -1)

    elif(y >= 0.15866 and y < 0.21186):
        x = obtenerX(y, 0.15866, 0.21186, -1, -0.8)

    elif(y >= 0.21186 and y < 0.27425):
        x = obtenerX(y, 0.21186, 0.27425, -0.8, -0.6)

    elif(y >= 0.27425 and y < 0.34458):
        x = obtenerX(y, 0.27425, 0.34458, -0.6, -0.4)

    elif(y >= 0.34458 and y < 0.42074):
        x = obtenerX(y, 0.34458, 0.42074, -0.4, -0.2)

    elif(y >= 0.42074 and y < 0.5):
        x = obtenerX(y, 0.42074, 0.5, -0.2, 0)

    elif(y >= 0.5 and y < 0.57926):
        x = obtenerX(y, 0.5, 0.57926, 0, 0.2)

    elif(y >= 0.57926 and y < 0.65542):
        x = obtenerX(y, 0.57926, 0.65542, 0.2, 0.4)

    elif(y >= 0.65542 and y < 0.72575):
        x = obtenerX(y, 0.65542, 0.72575, 0.4, 0.6)

    elif(y >= 0.72575 and y < 0.78814):
        x = obtenerX(y, 0.72575, 0.78814, 0.6, 0.8)

    elif(y >= 0.78814 and y < 0.84134):
        x = obtenerX(y, 0.78814, 0.84134, 0.8, 1)

    elif(y >= 0.84134 and y < 0.88493):
        x = obtenerX(y, 0.84134, 0.88493, 1, 1.2)

    elif(y >= 0.88493 and y < 0.93319):
        x = obtenerX(y, 0.88493, 0.93319, 1.2, 1.5)

    elif(y >= 0.93319 and y < 0.97725):
        x = obtenerX(y, 0.93319, 0.97725, 1.5, 2)

    elif(y >= 0.97725 and y < 0.99379):
        x = obtenerX(y, 0.97725, 0.99379, 2, 2.5)

    elif(y >= 0.99379 and y < 0.99865):
        x = obtenerX(y, 0.99379, 0.99865, 2.5, 3)

    elif(y >= 0.99865 and y < 0.9997):
        x = obtenerX(y, 0.99865, 0.9997, 3, 4)
    else:
        x = obtenerX(y, 0.9997, 1, 4, 5)

    return x


# Paso 1: Generamos muestras de la variable uniforme U
x_n = constante.SEMILLA
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa
for i in range(len(u)):
    x.append(obtenerTransfInversa(u[i]))  # Transformacion inversa

# Mostramos histograma del resultado
data = [go.Histogram(x=x)]
py.plot(data, filename='histograma-inversa-normal-v1')

# Mostramos meida, varianza y moda muestrales y teoricos
media = np.mean(x)
varianza = np.var(x)
moda = stats.mode(x).mode[0]  # tengo un solo array, i.e. una sola moda

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(
    media, varianza, moda))
print(
    "Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(0, 1, 0))
