import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp
from math import sqrt

import numpy as np
import scipy.stats as st


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


def encontrar_max_distancia():
    maximo = 0
    funcionDistribucionNormal = st.norm(35, 25)

    for indice, unaMuestra in enumerate(muestra, start=1):
        resta = indice/float(cantidadMuestras) - funcionDistribucionNormal.cdf(unaMuestra) 
        
        if resta < 0:
            resta *= -1
        
        if resta > maximo:
            maximo = resta

    return maximo

def verificar_hipotesis(maximo,tamanioMuestra):
    exponente = -1 * 2 * tamanioMuestra * 0.01 * 0.01

    alpha = 1 - exp(exponente)

    radicando = ( -1 * ( 1 / float( 2 * tamanioMuestra ) ) ) * log( alpha / float(2))

    return sqrt( radicando )

#------------------------------------------------------

muestra = []  # array de normales
cantidadMuestras = 100000

for _ in range(cantidadMuestras):
    x_n = generador_aceptacion_rechazon_variable_normal()
    muestra.append(x_n)

muestra.sort()

maximaDist = encontrar_max_distancia()

print("max x hallado -->  | F(x) - F(x) |: {0} ".format(maximaDist))

parametroDeRechazo = verificar_hipotesis(maximaDist,cantidadMuestras)

if maximaDist > parametroDeRechazo:
    print("Se aprueba el test")
    print("q = {0} > {1}").format(maximaDist,parametroDeRechazo)
else:
    print("No se aprueba el test")
    print("q = {0} < {1}").format(maximaDist,parametroDeRechazo)
