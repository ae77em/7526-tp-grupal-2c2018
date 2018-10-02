import plotly.plotly as py
import plotly.graph_objs as go
import random

from math import log
from math import exp


def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x

def calcularEst(Oi,Ei):

    return ( pow( Oi - Ei ,2) ) / float(Ei)

def obtenerProbabilidadDeGap(nroDeGap):

    return (0.8)*pow(0.2,nroDeGap)


x_n = (90697 + 89563) // 2

gapsPrimerIntervalo = []  # array de nro generado
contadorPrimerIntervalo = 0
aparecioPrimerNroEnPrimerRango = False

gapsSegundoIntervalo = []  # array de nro generado
contadorSegundoIntervalo = 0
aparecioPrimerNroEnSegundoRango = False

for i in range(30):
    x_n = generador_congruencial_lineal(x_n)

    if x_n >= 0.2 and x_n <= 0.6:
        if aparecioPrimerNroEnPrimerRango == False:
            aparecioPrimerNroEnPrimerRango = True
        else:
            contadorPrimerIntervalo -= 1
            gapsPrimerIntervalo.append(contadorPrimerIntervalo)
            contadorPrimerIntervalo = 0

    if x_n >= 0.5 and x_n <= 1:
        if aparecioPrimerNroEnSegundoRango == False:
            aparecioPrimerNroEnSegundoRango = True
        else:
            contadorSegundoIntervalo -= 1
            gapsSegundoIntervalo.append(contadorSegundoIntervalo)
            contadorSegundoIntervalo = 0

    #si aparecio por primera vez, va incrementandose hasta q se resetea
    if aparecioPrimerNroEnPrimerRango == True:
        contadorPrimerIntervalo += 1

    if aparecioPrimerNroEnSegundoRango == True:
        contadorSegundoIntervalo += 1

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

for unGap in gapsSegundoIntervalo:
    if str(unGap) in counters:
        counters[str(unGap)] = counters[str(unGap)] + 1
    else:
        counters[str(unGap)] = 1

    if maxGap < unGap:
        maxGap = unGap


#creo array del contenido como tantos gaps existan
contadorGaps = [0] * (maxGap + 1)

#sort gaps de menor a mayor
for key, value in counters.iteritems():
    contadorGaps[int(key)] = value
    totalGap += value

print "TOTAL GAPS"
print totalGap
print ""
print "GAPS"
print contadorGaps

print("i" ,"p","Oi","Ei")
sumar = 0
for key, value in enumerate(contadorGaps):
    probabilidadDeGap = obtenerProbabilidadDeGap(key)
    Ei = probabilidadDeGap * totalGap
    Oi = value

    sumar += Ei

    print(key ,probabilidadDeGap,Oi,Ei, calcularEst(Oi,Ei))

print ""
print "SUM Ei"
print sumar

