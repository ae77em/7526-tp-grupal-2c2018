import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
import numpy as np

from funciones import gcl_uniforme

import constante

def generar_histograma(numeros_aleatorios):
    plt.hist(numeros_aleatorios)
    plt.title("Histograma GCL")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")

    fig = plt.gcf()
    plotly_fig = tls.mpl_to_plotly( fig )
    py.plot(plotly_fig, filename='histograma-gcl')

## resolucion de histograma
x_n = constante.SEMILLA
numeros_aleatorios = []

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    numeros_aleatorios.append(x_n)

generar_histograma(numeros_aleatorios)
