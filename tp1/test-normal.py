import numpy as np
import scipy.stats as stats
import pylab as pl
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
import random

from math import log
from math import exp
from math import sqrt
from math import e
from math import pi

import constante
from funciones import normal_por_aceptacion_rechazo

z = normal_por_aceptacion_rechazo(media=35, de=5)

hist_data = [z]

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, [""], bin_size=.01, curve_type='normal')

fig['layout'].update(title='Normal empirica vs Normal de python')

# Plot!
py.plot(fig, filename='normal empirica vs normal de python')

# Mostramos media, varianza y moda muestrales y teoricos
media = np.mean(z)
varianza = np.var(z)
moda = stats.mode(z).mode[0]  # tengo un solo array, i.e. una sola moda

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(
    media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(
    35, 5*5, 35))