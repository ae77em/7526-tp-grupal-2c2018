import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp
import scipy.stats as stats

from funciones import gcl_uniforme
import constante

def calcularEst(Oi,Ei):
    if Ei == 0:
        return 0
    return ( ( ( Oi - Ei )**2 ) ) / (Ei)

def obtenerProbabilidadDeGap(nroDeGap):
    return (0.5)*pow(0.5,nroDeGap)*constante.CANT_EXPERIMENTOS


x_n = constante.SEMILLA

gapsPrimerIntervalo = []  # array de nro generado
contadorGap = 0
aparecioPrimerNroEnPrimerRango = False

i = 1

while i < constante.CANT_EXPERIMENTOS:
    x_n = gcl_uniforme(x_n)

    if x_n >= 0.5 and x_n <= 1:
        gapsPrimerIntervalo.append(contadorGap)
        contadorGap = 0
        i += 1
    else:
        contadorGap += 1


maxGap = 0
totalGap = 0
counters = {}

for unGap in gapsPrimerIntervalo:
    if str(unGap) in counters:
        counters[str(unGap)] = counters[str(unGap)] + 1
    else:
        counters[str(unGap)] = 1

    if maxGap < unGap:
        maxGap = unGap

#creo array del contenido como tantos gaps existan
contadorGaps = [0] * (maxGap + 1)

#creo array para valores esperados
valoresEsperados = [0] * (maxGap + 1)

for key, value in counters.iteritems():
    contadorGaps[int(key)] = value

for i in range(0,maxGap-1):
    valoresEsperados[i] = obtenerProbabilidadDeGap(i)

Dsquared = 0

for key, value in enumerate(contadorGaps):
    Ei = valoresEsperados[key]
    Oi = value

    Dsquared += calcularEst(Oi,Ei)

t = stats.chi2.ppf(q=0.95, df=1)

print ("Aplicamos test chi cuadrado a los resultados de test gap.")
print ("t: ", t)
print ("D2 : ", Dsquared)

if (Dsquared < t):
    print('''
    ACEPTAMOS la hipotesis con un error del 5% para el gap test con intervalo [0.5, 1].
    ''')
else:
    print('''
    RECHAZAMOS la hipotesis con un error del 5% para el gap test con intervalo [0.5, 1].
    ''')