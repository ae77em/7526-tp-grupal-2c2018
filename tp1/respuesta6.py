import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import matplotlib.pyplot as plt

from geometrica_empirica import experimento_geometrica

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
