import numpy
from numpy import linalg
import matplotlib.pyplot as plt

def get_next_state(xt):
    xtplus1 = 0

    if (xt == 0):
        a = numpy.arange(xt, xt+2)
        xtplus1 = numpy.random.choice(a, p=[39.0/40.0, 1.0/40.0])
    elif (xt == 29):
        a = numpy.arange(xt, xt+2)
        xtplus1 = numpy.random.choice(numpy.arange(xt, xt-2), p=[29.0/30.0, 1.0/30.0])
    else:
        a = numpy.arange(xt-1, xt+2)
        xtplus1 = numpy.random.choice(numpy.arange(xt-1, xt+2), p=[1.0/30.0, 113.0/120.0, 1.0/40.0])

    return xtplus1

def steady_state_prop(p):
    dim = p.shape[0]
    q = (p-numpy.eye(dim))
    ones = numpy.ones(dim)
    q = numpy.c_[q,ones]
    QTQ = numpy.dot(q, q.T)
    bQT = numpy.ones(dim)
    return numpy.linalg.solve(QTQ,bQT)

states = 30
N = 1000 * (1000/10) # 1000 secs == 10000 miliseconds
P = numpy.loadtxt("respuesta2_matriz.csv", delimiter=",")
I = numpy.matrix([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
Pn = numpy.zeros(states, dtype=float)

Pn = I * P
n = 1

while n <= N:
    Pn = Pn * P
    n += 1    
    
steady = steady_state_prop(P)

# imprimo porcentaje de tiempo en que el sistema estuvo vacio
print ('Porcentaje en 0: %.8f%%' % (float(steady[0] * 100)))

states = []
xn = 0

for i in range(N):
    xn = get_next_state(xn)
    states.append(xn)

# ploteo valores en cada momento
plt.plot(states)
plt.show()

# ploteo histograma
plt.xticks(numpy.arange(30))
plt.hist(states, bins=31) 
plt.title("Cantidad de veces en cada estado cada 10 mseg durante 1000 segundos")
plt.show()