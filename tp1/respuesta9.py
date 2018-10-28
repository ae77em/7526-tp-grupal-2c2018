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


def gap_test(alfa, beta):
    x_n = constante.SEMILLA

    gaps = []  # array de nro generado
    gap = 0
    i = 0

    while i < constante.CANT_EXPERIMENTOS:
        x_n = gcl_uniforme(x_n)

        if ((x_n<alfa) or (x_n>=beta)):
            gap = gap + 1
        else:
            gaps.append(gap)
            gap = 0
            i = i + 1

    maxGap = max(gaps)
    counters = {}

    for unGap in gaps:
        if str(unGap) in counters:
            counters[str(unGap)] = counters[str(unGap)]
        else:
            counters[str(unGap)] = 0

    # creo array del contenido como tantos gaps existan
    contadorGaps = [0] * (maxGap+1)
    for key, value in counters.iteritems():
        print(key)
        contadorGaps[int(key)] = value

    print("contadorGaps", contadorGaps, len(contadorGaps))

    # creo array para valores esperados
    valoresEsperados = [0] * (maxGap)
    for i in range(maxGap+1):
        valoresEsperados[i] = obtenerProbabilidadDeGap(alfa, beta, i) * constante.CANT_EXPERIMENTOS

    print("valoresEsperados", valoresEsperados, len(valoresEsperados))

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
            alfa, beta))
    else:
        print("RECHAZAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(
            alfa, beta))


gap_test(0.2, 0.6)
gap_test(0.5, 1)
