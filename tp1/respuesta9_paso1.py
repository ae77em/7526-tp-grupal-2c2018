import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp
import scipy.stats as stats

cant = 100000

def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x

def calcularEst(Oi,Ei):
    if Ei == 0:
        return 0
    return ( ( ( Oi - Ei )**2 ) ) / (Ei)

def obtenerProbabilidadDeGap(nroDeGap):
    return (0.5)*pow(0.5,nroDeGap)*cant


x_n = (90697 + 89563) // 2

gapsPrimerIntervalo = []  # array de nro generado
contadorGap = 0
aparecioPrimerNroEnPrimerRango = False

i = 1

while i < cant:
    x_n = generador_congruencial_lineal(x_n)

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

print "MAX GAPS"
print maxGap

print ""
print "GAPS"
print contadorGaps
print ""
print "valores esperados"
print valoresEsperados

Dsquared = 0

for key, value in enumerate(contadorGaps):
    Ei = valoresEsperados[key]
    Oi = value

    print(key ,value,valoresEsperados[key], calcularEst(Oi,Ei))
    Dsquared += calcularEst(Oi,Ei)

t = stats.chi2.ppf(q=0.95, df=1)

print ("resultado de la chi 2 --> t: ",t)
print ("D2 : ",Dsquared)