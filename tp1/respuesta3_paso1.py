'''
Ejercicio 2
Utilizando el generador de numeros aleatorios con distribucion uniforme [0,1] implementado en el ejercicio 1 y utilizando
el metodo de la transformada inversa genere numeros pseudoaleatorios con distribucion exponencial negativa de media
15.
 * Realizar un histograma de 100.000 valores obtenidos.
 * Calcular la media, varianza y moda de la distribucion obtenida y compararlos con los valores teoricos.
'''
import plotly.plotly as py
import plotly.graph_objs as go

from math import log

# funciones auxiliares


def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x


def obtenerX(y, y1, y2, x1, x2):
    return x1 + (y - y1)*(x2 - x1) * (1 / (y2 - y1))


def obtenerTransfInversa(y):
    x = 0

    if(y >= 0 & y < 0.0003):
        x = obtenerX(y, 0, 0.0003, -5, -4)

    elif(y >= 0.0003 & y < 0.00135):
        x = obtenerX(y, 0.0003, 0.00135 , -4, -3)

    elif(y >= 0.00135 & y < 0.00621):
            x = obtenerX(y, 0.00135, 0.00621, -3, -2.5)

    elif(y >= 0.00621 & y < 0.02275):
            x = obtenerX(y, 0.00621, 0.02275, -2.5, -2)

    elif(y >= 0.02275 & y < 0.06681):
            x = obtenerX(y, 0.02275, 0.06681, -2, -1.5)

    elif(y >= 0.06681 & y < 0.11507):
            x = obtenerX(y, 0.06681, 0.11507, -1.5, -1.2)

    elif(y >= 0.11507 & y < 0.15866):
            x = obtenerX(y, 0.11507, 0.15866, -1.2, -1)

    elif(y >= 0.15866 & y < 0.21186):
            x = obtenerX(y, 0.15866, 0.21186, -1, -0.8)

    elif(y >= 0.21186 & y < 0.27425):
            x = obtenerX(y, 0,21186, 0.27425, -0.8, -0.6)

    elif(y >= 0.27425 & y < 0.34458):
            x = obtenerX(y, 0.27425, 0.34458, -0.6, -0.4)

    elif(y >= 0.34458 & y < 0.42074):
            x = obtenerX(y, 0.34458, 0.42074, -0.4, -0.2)

    elif(y >= 0.42074 & y < 0.5):
            x = obtenerX(y, 0.42074, 0.5, -0.2, 0)

    elif(y >= 0.5 & y < 0.57926):
            x = obtenerX(y, 0.5, 0.57926, 0, 0.2)

    elif(y >= 0.57926 & y < 0.65542):
            x = obtenerX(y, 0.57926, 0.65542, 0.2, 0.4)

    elif(y >= 0.65542 & y < 0.72575):
            x = obtenerX(y, 0.65542, 0.72575, 0.4, 0.6)

    elif(y >= 0.72575 & y < 0.78814):
            x = obtenerX(y, 0.72575, 0.78814, 0.6, 0.8)

    elif(y >= 0.78814 & y < 0.84134):
            x = obtenerX(y, 0.78814, 0.84134, 0.8, 1)

    elif(y >= 0.84134 & y < 0.88493):
            x = obtenerX(y, 0.84134, 0.88493, 1, 1.2)

    elif(y >= 0.88493 & y < 0.93319):
            x = obtenerX(y, 0.88493, 0.93319, 1.2, 1.5)

    elif(y >= 0.93319 & y < 0.97725):
            x = obtenerX(y, 0.93319, 0.97725, 1.5, 2)

    elif(y >= 0.97725 & y < 0.99379):
            x = obtenerX(y, 0.97725, 0.99379, 2, 2.5)

    elif(y >= 0.99379 & y < 0.99865):
            x = obtenerX(y, 0.99379, 0.99865, 2.5, 3)

    elif(y >= 0.99865 & y < 0.9997):
            x = obtenerX(y, 0.99865, 0.9997, 3, 4)
    else:
            x = obtenerX(y, 0.9997, 1, 4, 5)

    return x

# Paso 1: Generamos muestras de la variable uniforme U
x_n = (90697 + 89563) // 2
u = []  # array de uniformes
x = []  # array de inversas

for _ in range(100000):
    x_n = generador_congruencial_lineal(x_n)
    u.append(x_n)

#  Paso 2: Aplicar la transformacion inversa
for i in range(len(u)):
    x.append( obtenerTransfInversa(i) )  # Transformacion inversa

# Mostramos histograma del resultado
data = [go.Histogram(x=x)]
py.plot(data, filename='histograma-inversa')
