'''
Ejercicio 1
Utilizando Matlab, Octave o Python implementar un Generador Congruencial Lineal (GCL) de modulo 232, multiplicador
1013904223, incremento de 1664525 y semilla igual a la parte entera del promedio de los numeros de padron de los
integrantes del grupo.
 * Informar los primeros 6 numeros al azar de la secuencia.
 * Modificar el GCL para que devuelva numeros al azar entre 0 y 1, y realizar un histograma sobre 100.000 valores generados.
'''
import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
import numpy as np

## funciones auxiliares

def newmethod480():
    def generador_congruencial_lineal(x_n):
        m = 232                     # modulus
        a = 1013904223              # multiplier
        c = 1664525                 # increment

        x = float(((a * x_n) + c) % m) / float(m)

        return x
    return generador_congruencial_lineal

generador_congruencial_lineal = newmethod480()

def generar_histograma(numeros_aleatorios):
    plt.hist(numeros_aleatorios)
    plt.title("Histograma GCL")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")

    fig = plt.gcf()
    plotly_fig = tls.mpl_to_plotly( fig )
    py.plot(plotly_fig, filename='histograma-gcl')

## resolucion de histograma
x_n = (90697 + 89563) // 2
numeros_aleatorios = []

for _ in range(100000):
    x_n = generador_congruencial_lineal(x_n)
    numeros_aleatorios.append(x_n)

generar_histograma(numeros_aleatorios)
