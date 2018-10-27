import random
import statistics as st
from math import e, exp, log, pi, sqrt

import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly.plotly as py
import pylab as pl
import scipy.stats as stats

import constante
from funciones import normal_por_aceptacion_rechazo

z = normal_por_aceptacion_rechazo(media=35, de=5)

hist_data = [z]

# ploteo data
fig = ff.create_distplot(hist_data, [""], bin_size=.01, curve_type='normal')
fig['layout'].update(title='Normal empirica vs Normal de python')
py.plot(fig, filename='normal empirica vs normal de python')

# Mostramos media, varianza y moda muestrales y teoricos
media = st.mean(z)
varianza = st.variance(z)
moda = max(set(z), key=z.count)

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(35, 5*5, 35))
