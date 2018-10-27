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

