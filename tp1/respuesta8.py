# RESPUESTA 8
import scipy.stats as stats

from funciones import experimento_geometrica
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
    Dsquared = Dsquared + ((observados[i] - esperados[i]) ** 2) / esperados[i]

t = stats.chi2.ppf(q=0.99, df=1)

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
