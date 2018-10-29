# CONSTANTE
SEMILLA = (90697 + 89563) // 2
CANT_EXPERIMENTOS = 100000

# FUNCIONES
import random

from math import log
from math import exp
from math import sqrt
from math import e
from math import pi

import constante

#
# Retorna un valor entre 0 y 1 usando el algoritmo gcl
#
def gcl_uniforme(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x

#
# Simula 100000 lanzamientos de una moneda con probabilidad p de sacar cara
#
def experimento_geometrica(p):
    # genero numero aleatorios uniformes
    x_n = constante.SEMILLA
    empiricos = []

    # hago el experimento
    for _ in range(constante.CANT_EXPERIMENTOS):
        salio1 = False
        lanzamientos = 0
        
        while not salio1:
            x_n = gcl_uniforme(x_n)
            lanzamientos = lanzamientos + 1

            if (x_n >= 1-p) and (x_n < 1):
                salio1 = True
                empiricos.append(lanzamientos)

    return empiricos

#
# Funcion H
#
def funcionH(unNro):
    result = (pow(unNro - 1, 2) * 1) / 2
    return exp(result)

#
# Algoritmo de aceptacion/rechazo
#

def normal_por_aceptacion_rechazo(media=0, de=1):
    """
    Calcula la normal con 100000 simulaciones, usando el metodo de aceptacion/rechazo.
    
    Parametros:
    
    media: el valor de la media de la normal a calcular
    
    de: el valor de la desviacion estandar de la normal a calcular
    """
    c = sqrt(2*e/pi)
    cant = constante.CANT_EXPERIMENTOS
    j = 0
    u = [0] * constante.CANT_EXPERIMENTOS # array de normales

    while(j < cant):
        # Utilizamos el metodo de la transformada inversa para calcular la exponencial
        u1 = random.uniform(0, 1)
        r1 = -1*log(1-u1)
        u2 = random.uniform(0, 1)

        if (2*pow(e, -1*pow(r1, 2)/2)/sqrt(2*pi)/(pow(e,-r1)*c) >= u2):
            u3 = random.uniform(0, 1)
            
            if (u3 > 0.5):
                u[j] = float(de) * r1 + media
            else:
                u[j] = -float(de) * r1 + media
            
            j = j+1

    return u

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
# RESPUESTA 10 paso 2
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


x = []  # array de normales
yEmpirica = []  # array de normales
yReal = []  # array de normales

funcionDistribucionNormal = st.norm(35, 5)

cantidadMuestras = constante.CANT_EXPERIMENTOS

muestra = normal_por_aceptacion_rechazo(35, 5)
muestra.sort()

for indice, unaMuestra in enumerate(muestra, start=1):
    x.append(unaMuestra)
    yEmpirica.append(indice/float(cantidadMuestras))
    yReal.append(funcionDistribucionNormal.cdf(unaMuestra))

trace0 = go.Scatter(
    x=x,
    y=yEmpirica,
    mode='lines+markers',
    name='empirica',    
    marker = dict(
          color = 'rgb(231, 99, 250, 0.5)',
          size = 0.1
        )
)
trace1 = go.Scatter(
    x=x,
    y=yReal,
    mode='lines+markers',
    name='real',
    marker = dict(
          color = 'rgba(17, 157, 255, 0.5)',
          size = 0.1
        )
)

data = [trace0, trace1]

py.plot(data, filename='test-smirnov-normal-empirica-vs-real')
# RESPUESTA 1 paso 1
import constante

def gcl(x_n):
   m = 232                     # modulus
   a = 1013904223              # multiplier
   c = 1664525                 # increment

   x = ((a * x_n) + c) % m

   return x

x_n = constante.SEMILLA

for _ in range(6):
   x_n = gcl(x_n)
   print(x_n)
# RESPUESTA 1 paso 2
import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
import numpy as np

from funciones import gcl_uniforme

import constante

def generar_histograma(numeros_aleatorios):
    plt.hist(numeros_aleatorios)
    plt.title("Histograma GCL")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")

    fig = plt.gcf()
    plotly_fig = tls.mpl_to_plotly( fig )
    py.plot(plotly_fig, filename='histograma-gcl')

## resolucion de histograma
x_n = constante.SEMILLA
numeros_aleatorios = []

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    numeros_aleatorios.append(x_n)

generar_histograma(numeros_aleatorios)
# RESPUESTA 2
import numpy as np
from scipy import stats
from math import log

import plotly.plotly as py
import plotly.graph_objs as go

from funciones import gcl_uniforme
import constante

# Paso 1: Generamos muestras de la variable uniforme U
x_n = constante.SEMILLA
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa
paramLambda = float(1)/float(15)
for i in range(len(u)):
    x.append(-log(1-u[i])/paramLambda)  # Transformacion inversa

# Mostramos histograma del resultado
data = [go.Histogram(x=x)]
py.plot(data, filename='histograma-inversa-exponencial')

# Mostramos media, varianza y moda muestrales y teoricos
media = np.mean(x)
varianza = np.var(x)
moda = max(set(x), key=x.count)  

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(15, 15*15, 0))
# RESPUESTA 3 version 1
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

from math import log
from scipy import stats
from scipy.interpolate import interp1d

from funciones import gcl_uniforme
import constante


def obtenerX(y, y1, y2, x1, x2):
    return x1 + (y - y1)*(x2 - x1) * (1 / (y2 - y1))


def obtenerTransfInversa(y):
    x = 0

    if(y >= 0 and y < 0.0003):
        x = obtenerX(y, 0, 0.0003, -5, -4)

    elif(y >= 0.0003 and y < 0.00135):
        x = obtenerX(y, 0.0003, 0.00135, -4, -3)

    elif(y >= 0.00135 and y < 0.00621):
        x = obtenerX(y, 0.00135, 0.00621, -3, -2.5)

    elif(y >= 0.00621 and y < 0.02275):
        x = obtenerX(y, 0.00621, 0.02275, -2.5, -2)

    elif(y >= 0.02275 and y < 0.06681):
        x = obtenerX(y, 0.02275, 0.06681, -2, -1.5)

    elif(y >= 0.06681 and y < 0.11507):
        x = obtenerX(y, 0.06681, 0.11507, -1.5, -1.2)

    elif(y >= 0.11507 and y < 0.15866):
        x = obtenerX(y, 0.11507, 0.15866, -1.2, -1)

    elif(y >= 0.15866 and y < 0.21186):
        x = obtenerX(y, 0.15866, 0.21186, -1, -0.8)

    elif(y >= 0.21186 and y < 0.27425):
        x = obtenerX(y, 0.21186, 0.27425, -0.8, -0.6)

    elif(y >= 0.27425 and y < 0.34458):
        x = obtenerX(y, 0.27425, 0.34458, -0.6, -0.4)

    elif(y >= 0.34458 and y < 0.42074):
        x = obtenerX(y, 0.34458, 0.42074, -0.4, -0.2)

    elif(y >= 0.42074 and y < 0.5):
        x = obtenerX(y, 0.42074, 0.5, -0.2, 0)

    elif(y >= 0.5 and y < 0.57926):
        x = obtenerX(y, 0.5, 0.57926, 0, 0.2)

    elif(y >= 0.57926 and y < 0.65542):
        x = obtenerX(y, 0.57926, 0.65542, 0.2, 0.4)

    elif(y >= 0.65542 and y < 0.72575):
        x = obtenerX(y, 0.65542, 0.72575, 0.4, 0.6)

    elif(y >= 0.72575 and y < 0.78814):
        x = obtenerX(y, 0.72575, 0.78814, 0.6, 0.8)

    elif(y >= 0.78814 and y < 0.84134):
        x = obtenerX(y, 0.78814, 0.84134, 0.8, 1)

    elif(y >= 0.84134 and y < 0.88493):
        x = obtenerX(y, 0.84134, 0.88493, 1, 1.2)

    elif(y >= 0.88493 and y < 0.93319):
        x = obtenerX(y, 0.88493, 0.93319, 1.2, 1.5)

    elif(y >= 0.93319 and y < 0.97725):
        x = obtenerX(y, 0.93319, 0.97725, 1.5, 2)

    elif(y >= 0.97725 and y < 0.99379):
        x = obtenerX(y, 0.97725, 0.99379, 2, 2.5)

    elif(y >= 0.99379 and y < 0.99865):
        x = obtenerX(y, 0.99379, 0.99865, 2.5, 3)

    elif(y >= 0.99865 and y < 0.9997):
        x = obtenerX(y, 0.99865, 0.9997, 3, 4)
    else:
        x = obtenerX(y, 0.9997, 1, 4, 5)

    return x


# Paso 1: Generamos muestras de la variable uniforme U
x_n = constante.SEMILLA
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa
for i in range(len(u)):
    x.append(obtenerTransfInversa(u[i]))  # Transformacion inversa

# Mostramos histograma del resultado
data = [go.Histogram(x=x)]
#py.plot(data, filename='histograma-inversa-normal-v1')

# Mostramos media, varianza y moda muestrales y teoricos
media = np.mean(x)
varianza = np.var(x)
moda = max(set(x), key=x.count)  

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(0, 1, 0))
# RESPUESTA 3 version 2
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

from math import log
from scipy import stats
from scipy.interpolate import interp1d

from funciones import gcl_uniforme
import constante
# Paso 1: Generamos muestras de la variable uniforme U
x_n = constante.SEMILLA
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa, usando interpolacion lineal, con los rangos dados en apunte
x_coords = [ 0, 0.00003, 0.00135, 0.00621, 0.02275, 0.06681, 0.11507, 0.15866, 0.21186, 0.27425, 0.34458, 0.42074, 0.5, 0.57926, 0.65542, 0.72575, 0.78814, 0.84134, 0.88493, 0.93319, 0.97725, 0.99379, 0.99865, 0.99997, 1]
y_coords = [-5,      -4,      -3,    -2.5,      -2,    -1.5,    -1.2,      -1,    -0.8,    -0.6,    -0.4,    -0.2,   0,     0.2,     0.4,     0.6,     0.8,       1,     1.2,     1.5,       2,     2.5,       3,       4, 5]

f_inversa = interp1d(x_coords, y_coords)

x = f_inversa(u)  # Transformacion inversa

# Mostramos histograma del resultado
data = [go.Histogram(x=x)]
#py.plot(data, filename='histograma-inversa-normal-v2')

# Mostramos media, varianza y moda muestrales y teoricos
media = np.mean(x)
varianza = np.var(x)
moda = max(set(x.tolist()), key=x.tolist().count)

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(0, 1, 0))

# RESPUESTA 4
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
# RESPUESTA 5
from funciones import gcl_uniforme
import constante

# genero numero aleatorios uniformes
x_n = constante.SEMILLA
uniformes = []
empiricos = []

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    uniformes.append(x_n)

# la funcion definida por la tabla en el enunciado es:
# f(x) = I{ 0 <= x < 0.5}  + 2 * I{ 0.5 <= x < 0.7} + 3 * I{ 0.7 <= x < 0.8} + 4 * I{ 0.8 <= x < 1}
# Luego:
for nro in uniformes:
    if (nro >= 0 and nro < 0.5):
        empiricos.append(1)
    elif (nro >= 0.5 and nro < 0.7):
        empiricos.append(2)
    elif (nro >= 0.7 and nro < 0.8):
        empiricos.append(3)
    else:
        empiricos.append(4)

print(empiricos)
# RESPUESTA 6
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import matplotlib.pyplot as plt

from funciones import experimento_geometrica

# hago los experimentos
datos_equilibrada = experimento_geometrica(0.5)
data = [go.Histogram(x=datos_equilibrada )]
py.plot(data, filename='histograma-moneda-equilibrada')
# RESPUESTA 7 paso 1
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from funciones import gcl_uniforme
import constante

x_n = constante.SEMILLA
u = []
v = []

for i in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)

    if (i % 2 == 0):
        u.append(x_n)
    else:
        v.append(x_n)

trace = go.Scatter(
    x=u,
    y=v,
    mode='markers',
    marker=dict(
        size=3,
        color="#4faab4",
        colorscale='Viridis',
    ),
)

data = [trace]

py.plot(data, filename='test-espectral-2d-gcl')
# RESPUESTA 7 paso 2
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from funciones import gcl_uniforme
import constante

x_n = constante.SEMILLA
u = []  
v = []  
w = []
k = 0

for i in range(constante.CANT_EXPERIMENTOS):
    x_n = gcl_uniforme(x_n)
    
    if (k % 3 == 0):
        u.append(x_n)
        k = 0
    if (k % 2 == 0):
        v.append(x_n)
        k = k+1
    else:
        w.append(x_n)
        k = k+1

trace = go.Scatter3d(
    x=u, y=v, z=w,
    marker=dict(
        size=1,
        color="#4faab4",
        colorscale='Viridis',
    ),
    line=dict(
        color='#1f77b4',
        width=1
    )
)

data = [trace]

layout = dict(
    width=800,
    height=700,
    autosize=False,
    title='Test espectral 3D de GCL',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        camera=dict(
            up=dict(
                x=0,
                y=0,
                z=1
            ),
            eye=dict(
                x=-1.7428,
                y=1.0707,
                z=0.7100,
            )
        ),
        aspectratio=dict(x=1, y=1, z=0.7),
        aspectmode='manual',        
    ),
)

fig = dict(data=data, layout=layout)

py.plot(fig, filename='test-espectral-3d-gcl', height=700)
# RESPUESTA 8
import scipy.stats as stats

from constante import CANT_EXPERIMENTOS

# tomamos los datos del histograma generado en punto 6
observados = [49712, 25070, 12519, 6366, 3155, 1618, 766, 381, 233, 92, 44, 25, 10, 5, 1, 3]

# la probabilidad se calcula como P(X = x) = (1-p)^(x-1) p 
esperados = []
cant_clases = len(observados)
n = CANT_EXPERIMENTOS
pAcumulada = 0
for x in range(1, cant_clases):
    p = (0.5 ** (x-1)) * 0.5
    pAcumulada = pAcumulada + p
    esperado = n * p 
    esperados.append(esperado)

# la ultima clase tiene una probabilidad p = 1 - suma(p esperados previos)
pUltimo = float(1) - pAcumulada
esperados.append(pUltimo * n)

Dsquared = 0
for i in range(cant_clases):
    Dsquared += ((observados[i] - esperados[i]) ** 2) / esperados[i]

# grados de libertad : (cantidad clases - 1)
t = stats.chi2.ppf(q=0.99, df=cant_clases - 1)

print("D^2 = " + str(Dsquared))
print("t = " + str(t))

print("Luego:")

if (Dsquared < t):
    print('''
    ACEPTAMOS que la distribucion empirica es una buena aproximacion 
    la distribucion geometrica con p = 0.5, con un error del 1%.
    ''')
else:
    print('''
    RECHAZAMOS que la distribucion empirica es una buena aproximacion 
    a la distribucion geometrica con p = 0.5, con un error del 1%.
    ''')

# RESPUESTA 9 bis
import scipy.stats as stats

import constante
from funciones import gcl_uniforme

def gap_test(alfa=0, beta=1):
    gaps = [0] * constante.CANT_EXPERIMENTOS
    i=0
    gap=0
    x_n = gcl_uniforme(constante.SEMILLA)

    while (i < constante.CANT_EXPERIMENTOS):
        if ((x_n < alfa) or (x_n >= beta)):
            gap += 1                 
        else:
            gaps[i] = gap + 1
            i += 1
            gap = 0
        
        x_n = gcl_uniforme(x_n)

    p = beta - alfa
    gapMax = max(gaps)

    # agrupo en 11 clases (de la 0 a la 10)
    observed = [0] * 11
    for i in range(10):
        observed[i] = gaps.count(i+1)

    for i in range(10, gapMax+1):
        observed[10] += gaps.count(i)

    expected = [0] * 11
    for i in range(10):
        expected[i] = p * ((1-p)**(i)) * constante.CANT_EXPERIMENTOS

    for i in range(10, gapMax+1):
        expected[10] += p * ((1-p)**(i-1)) * constante.CANT_EXPERIMENTOS

    print("observed", observed)
    print("expected", expected)

    Dsquared, p = stats.chisquare(observed, f_exp=expected)

    t = stats.chi2.ppf(q=0.95, df=10)

    print ("Aplicamos test chi cuadrado a los resultados de test gap.")
    print ("t: " + str(t))
    print ("D^2 : " + str(Dsquared))

    if (Dsquared < t):
        print("ACEPTAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(alfa, beta))
    else:
        print("RECHAZAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(alfa, beta))


gap_test(0.5, 1)
gap_test(0.2, 0.6)
    
# RESPUESTA 9
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
    contadorGaps = [0] * (maxGap)
    for key, value in counters.iteritems():
        print(key)
        contadorGaps[int(key)] = value

    print("contadorGaps", contadorGaps, len(contadorGaps))

    # creo array para valores esperados
    valoresEsperados = [0] * (maxGap)
    for i in range(maxGap):
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
