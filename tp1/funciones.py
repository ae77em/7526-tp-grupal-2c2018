import random

from math import log
from math import exp
from math import sqrt

import constante

def gcl_uniforme(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x

def experimento_geometrica(p):
    # genero numero aleatorios uniformes
    x_n = constante.SEMILLA
    empiricos = []

    # hago el experimento
    for _ in range(constante.CANT_EXPERIMENTOS):
        salio1 = False
        while not salio1:
            x_n = gcl_uniforme(x_n)
            
            if x_n >= 0.0 and x_n < 1-p:
                empiricos.append(0)
            else:
                empiricos.append(1)
                salio1 = True

    return empiricos

def funcionH(unNro):
    result = (pow(unNro - 1, 2) * 1) / 2

    return exp(result)

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