'''
Realizar un test Chi 2 a la distribucion empirica implementada en el Ej 6.
Analizar el resultado para un nivel de significacion 0,01.
'''
import scipy.stats as stats

from geometrica_empirica import experimento_geometrica

datos_cargada = []
datos_cargada = experimento_geometrica(0.3)

n0 = datos_cargada.count(0)
np0 = len(datos_cargada) * 0.7
n1 = datos_cargada.count(1)
np1 = len(datos_cargada) * 0.3

Dsquared = ((n0 - np0) ** 2) / np0 + ((n1 - np1) ** 2) / np1

t = stats.chi2.ppf(q=0.99, df=1)

print("D^2 = " + str(Dsquared))
print("t = " + str(t))

print("Luego:")

if (Dsquared < t):
    print('''
    ACEPTAMOS que la distribucion empirica es una buena aproximacion 
    la distribucion geometrica con p = 0.3, con un error del 1%.
    ''')
else:
    print('''
    RECHAZAMOS que la distribucion empirica es una buena aproximacion 
    a la distribucion geometrica con p = 0.3, con un error del 1%.
    ''')
