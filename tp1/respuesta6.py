# -*- coding: UTF-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import matplotlib.pyplot as plt

## funciones auxiliares
def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x

def experimento_geometrica(p):
    # genero numero aleatorios uniformes
    x_n = (90697 + 89563) // 2
    empiricos = []

    # hago el experimento
    for _ in range(10000):
        salio1 = False
        while not salio1:
            x_n = generador_congruencial_lineal(x_n)

            if (x_n >= 0.0 and x_n < 1-p):
                empiricos.append(0)
            else:
                empiricos.append(1)
                salio1 = True

    return empiricos

def ploteo_histograma(datos, filename):
    plt.hist(datos)
    plt.title("Histograma Geometrica")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")

    fig = plt.gcf()
    plotly_fig = tls.mpl_to_plotly(fig)
    py.plot(plotly_fig, filename=filename)


# hago los experimentos
datos_equilibrada = experimento_geometrica(0.5)
ploteo_histograma(datos_equilibrada,'histograma-moneda-equilibrada')

datos_cargada = experimento_geometrica(0.3)
ploteo_histograma(datos_cargada,'histograma-moneda-cargada')
