import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np


def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x


x_n = (90697 + 89563) // 2

gapsPrimerIntervalo = []  # array de nro generado
contadorPrimerIntervalo = 0
aparecioPrimerNroEnPrimerRango = False

gapsSegundoIntervalo = []  # array de nro generado
contadorSegundoIntervalo = 0
aparecioPrimerNroEnSegundoRango = False

for i in range(1000):
    x_n = generador_congruencial_lineal(x_n)

    if x_n >= 0.2 and x_n <= 0.6:
        if aparecioPrimerNroEnPrimerRango == False:
            aparecioPrimerNroEnPrimerRango = True
        else:
            gapsPrimerIntervalo.append(contadorPrimerIntervalo)
            contadorPrimerIntervalo = 0

    if x_n >= 0.5 and x_n <= 1:
        if aparecioPrimerNroEnSegundoRango == False:
            aparecioPrimerNroEnSegundoRango = True
        else:
            gapsSegundoIntervalo.append(contadorSegundoIntervalo)
            contadorSegundoIntervalo = 0

    if aparecioPrimerNroEnPrimerRango == True:
        contadorPrimerIntervalo += 1

    if aparecioPrimerNroEnSegundoRango == True:
        contadorSegundoIntervalo += 1

counters = {}

for unGap in gapsPrimerIntervalo:
    if str(unGap) in counters:
        counters[str(unGap)] = counters[str(unGap)] + 1
    else:
        counters[str(unGap)] = 1

for unGap in gapsSegundoIntervalo:
    if str(unGap) in counters:
        counters[str(unGap)] = counters[str(unGap)] + 1
    else:
        counters[str(unGap)] = 1

print counters

