# RESPUESTA 9 paso 2
import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp
import scipy.stats as stats

from funciones import gcl_uniforme
import constante


def calcularEst(Oi, Ei):
    if Ei == 0:
        return 0
    return (((Oi - Ei)**2)) / (Ei)


def obtenerProbabilidadDeGap(piso, techo, nroDeGap):
    pNroDeGap = techo - piso
    return (pNroDeGap * ((1-pNroDeGap) ** nroDeGap))


def evaluar_gap_test(piso, techo):
    x_n = constante.SEMILLA

    gapsPrimerIntervalo = []  # array de nro generado
    contadorGap = 0

    i = 1

    while i < constante.CANT_EXPERIMENTOS:
        x_n = gcl_uniforme(x_n)

        if x_n > piso and x_n < techo:
            gapsPrimerIntervalo.append(contadorGap)
            contadorGap = 0
            i = i + 1
        else:
            contadorGap = contadorGap + 1

    maxGap = 0
    counters = {}

    for unGap in gapsPrimerIntervalo:
        if str(unGap) in counters:
            counters[str(unGap)] = counters[str(unGap)] + 1
        else:
            counters[str(unGap)] = 1

        if maxGap < unGap:
            maxGap = unGap

    # creo array del contenido como tantos gaps existan
    contadorGaps = [0] * (maxGap + 1)

    # creo array para valores esperados
    valoresEsperados = [0] * (maxGap + 1)

    for key, value in counters.iteritems():
        contadorGaps[int(key)] = value

    for i in range(maxGap):
        valoresEsperados[i] = obtenerProbabilidadDeGap(
            piso, techo, i) * constante.CANT_EXPERIMENTOS

    Dsquared = 0

    for key, value in enumerate(contadorGaps):
        Ei = valoresEsperados[key]
        Oi = value

        Dsquared += calcularEst(Oi, Ei)

    t = stats.chi2.ppf(q=0.95, df=len(valoresEsperados) - 1)

    print ("Aplicamos test chi cuadrado a los resultados de test gap.")
    print ("t: " + str(t))
    print ("D^2 : " + str(Dsquared))

    if (Dsquared < t):
        print("ACEPTAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(
            piso, techo))
    else:
        print("RECHAZAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(
            piso, techo))


evaluar_gap_test(0.2, 0.6)
evaluar_gap_test(0.5, 1)
