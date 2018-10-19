# RESPUESTA 6
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import matplotlib.pyplot as plt

from funciones import experimento_geometrica

# hago los experimentos
datos_equilibrada = experimento_geometrica(0.5)
data = [go.Histogram(x=datos_equilibrada )]
py.plot(data, filename='histograma-moneda-equilibrada')
