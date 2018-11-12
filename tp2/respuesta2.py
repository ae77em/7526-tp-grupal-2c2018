"""
Un servidor recibe solicitudes las cuales son procesadas de una por vez en el orden de llegada (polItica FIFO).

Se determino que en 10 milisegundos existe una probabilidad p = 1.0/40.0 que llegue una nueva solicitud y una probabilidad
q = 1.0/30.0 que una solicitud termine de ser procesada y deje el sistema.

Se desea estudiar la cantidad de solicitudes en el servidor considerando tanto las que estan en cola esperando ser
procesadas como la solicitud que esta siendo procesada.

a. Determine la matriz de transicion de estados explicando como se obtiene la misma.

b. Simule la evolucion del sistema a lo largo de 1.0.000 segundos. Suponga que el
sistema puede tener como maximo 30.0 estados posibles y que el servidor comienza sin estar procesando solicitudes.

c. Realice un grafico mostrando la cantidad de solicitudes en el servidor en cada instante de tiempo.

d. Realice un histograma mostrando cuantas veces el sistema estuvo en cada estado.

e. Determine el % de tiempo que el servidor se encuentra sin procesar solicitudes.
"""

import numpy
from numpy import linalg

def steady_state_prop(p):
    dim = p.shape[0]
    q = (p-numpy.eye(dim))
    ones = numpy.ones(dim)
    q = numpy.c_[q,ones]
    QTQ = numpy.dot(q, q.T)
    bQT = numpy.ones(dim)
    return numpy.linalg.solve(QTQ,bQT)

states = 30
N = 1000
P = numpy.loadtxt("respuesta2_matriz.csv", delimiter=",")
I = numpy.matrix([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
Pn = numpy.zeros(states, dtype=float)
numberOfRequests = numpy.zeros(N)

Pn = I * P
n = 1
while n <= N:
    print(Pn)
    numberOfRequests[n-1] = numpy.count_nonzero(Pn) - 1
    print ("# Quantity of request in system after %i seconds -> %d" % (n, numberOfRequests[n-1]))
    Pn = Pn * P
    n += 1

