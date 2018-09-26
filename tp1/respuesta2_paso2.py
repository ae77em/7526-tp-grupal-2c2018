'''
Ejercicio 2
Utilizando el generador de numeros aleatorios con distribucion uniforme [0,1] implementado en el ejercicio 1 y utilizando
el metodo de la transformada inversa genere numeros pseudoaleatorios con distribucion exponencial negativa de media
15.
 * Realizar un histograma de 100.000 valores obtenidos.
 * Calcular la media, varianza y moda de la distribucion obtenida y compararlos con los valores teoricos.
'''
import numpy as np
from scipy import stats
from math import log

# funciones auxiliares
def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x

# Paso 1: Generamos muestras de la variable uniforme U
x_n = (90697 + 89563) // 2
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(100000):
    x_n = generador_congruencial_lineal(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa
paramLambda = float(1)/float(15)
for i in range(len(u)):
    x.append(-log(1-u[i])/paramLambda)  # Transformacion inversa

media = np.mean(x)
varianza = np.var(x)
moda = stats.mode(x).mode[0] # tengo un solo array, i.e. una sola moda

print("Media muestral: {0} Varianza muestral: {1} Moda muestral: {2}".format(media, varianza, moda))
print("Media teorica:  {0} Varianza teorica:  {1} Moda teorica:  {2}".format(15, 15*15, 0))
