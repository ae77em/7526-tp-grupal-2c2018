import random

from math import log
from math import exp
from math import sqrt

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
def generador_aceptacion_rechazon_variable_normal():
    U = 0
    continuar = True

    while(continuar):
        # genero variable con distribucion exp -1
        Y = -log(random.uniform(0, 1))
        U = random.uniform(0, 1)

        if U <= funcionH(Y):
            continuar = False

    if U < 0.5:
        return 5*Y + 35
    else:
        return -5*Y + 35
