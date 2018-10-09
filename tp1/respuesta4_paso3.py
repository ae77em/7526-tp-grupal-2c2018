import plotly.plotly as py
import plotly.graph_objs as go
import random

import numpy as np
from scipy import stats

from math import log
from math import exp

import constante


def funcionH(unNro):
    result = (pow(unNro - 1, 2) * 1) / 2

    return exp(result)

# funciones auxiliares


def generador_aceptacion_rechazon_variable_normal():
    U = 0
    count = 0
    continuar = True

    while(continuar):
        # genero variable con distribucion exp -1
        Y = log(random.uniform(0, 1)) * -1

        U = random.uniform(0, 1)

        count = count + 1

        if U <= funcionH(Y):
            continuar = False

    if U < 0.5:
        return 5*Y + 35
    else:
        return 5*Y*-1 + 35


# Paso 1: Generamos muestras de la variable uniforme U
u = []  # array de uniformes

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = generador_aceptacion_rechazon_variable_normal()
    u.append(x_n)

media = np.mean(u)
varianza = np.var(u)
moda = stats.mode(u).mode[0]  # tengo un solo array, i.e. una sola moda

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(
    media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(
    35, 5*5, 35))
