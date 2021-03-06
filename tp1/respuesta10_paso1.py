# RESPUESTA 10 paso 1
import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp
from math import sqrt

import numpy as np
import scipy.stats as st

from funciones import funcionH
from funciones import normal_por_aceptacion_rechazo
import constante


def encontrar_max_distancia():
    maximo = 0
    funcionDistribucionNormal = st.norm(35, 5)

    for indice, unaMuestra in enumerate(muestra, start=1):
        resta = indice/float(constante.CANT_EXPERIMENTOS) - \
            funcionDistribucionNormal.cdf(unaMuestra)

        if resta < 0:
            resta *= -1

        if resta > maximo:
            maximo = resta

    return maximo


def verificar_hipotesis(maximo, tamanioMuestra):
    exponente = -1 * 2 * tamanioMuestra * 0.01 * 0.01

    alpha = 1 - exp(exponente)

    radicando = (-1 * (1 / float(2 * tamanioMuestra))) * log(alpha / float(2))

    return sqrt(radicando)


muestra = normal_por_aceptacion_rechazo(media=35, de=5)

# ordeno las muestras de menor a mayor
muestra.sort()

# busco maxima distancia
maximaDist = encontrar_max_distancia()

print("max x hallado -->  | F(x) - F(x) |: {0} ".format(maximaDist))

parametroDeRechazo = verificar_hipotesis(maximaDist, constante.CANT_EXPERIMENTOS)

if maximaDist > parametroDeRechazo:
    print("Se aprueba el test")
    print("q = {0} > {1}").format(maximaDist, parametroDeRechazo)
else:
    print("No se aprueba el test")
    print("q = {0} < {1}").format(maximaDist, parametroDeRechazo)
