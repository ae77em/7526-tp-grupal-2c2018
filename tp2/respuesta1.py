"""
Punto 1

"""
import numpy
import random
import matplotlib.pylab as plt

arrives = 100000

def computeQueue(a, C, Q0=0): #  initial queue length is 0
    N = len(a)
    Q = numpy.zeros(N,dtype=int) # make a list to store the values of  Q
    d = numpy.zeros(N,dtype=int) # make a list to store the values of  d
    Q[0] = Q0
    for n in range(1,N):
        d[n] = min( Q[n-1] + a[n], C[n])
        Q[n] = Q[n-1] + a[n] - d[n]
    
    return Q, d

def waitingTime(At,Dt):
    # At[i] is the number of arrivals in time slot i
    # Convert this to the arrival time of each customer
    Ak = numpy.repeat(numpy.arange(len(At)), At)
    # Dt[i] is the number of departures in time slot i
    # Convert this to the departure time of each customer
    Dk = numpy.repeat(numpy.arange(len(Dt)), Dt)
    m = min(len(Ak), len(Dk))
    W = Dk[:m] - Ak[:m]
    
    return W

def capacidad_servidor(_lambda=1, _mu=1, _arrives=100000):
    baseArrivals = numpy.random.poisson(_lambda, size=int(_arrives))
    baseCapacity = _mu*numpy.ones_like(baseArrivals)

    queueSizes, departures = computeQueue(baseArrivals, baseCapacity)
        
    baseWaitingTime = waitingTime(baseArrivals, departures)
    
    print("El tiempo medio de espera es de %f segs" % baseWaitingTime.mean())
    aux = float(queueSizes.tolist().count(0)) / float(_arrives)
    print("Las solicitudes que no esperaron son el %f%%" % aux)

    resolutionTime = numpy.array([x + y for x, y in zip(baseWaitingTime, baseCapacity)])
    print("El tiempo de resolucion promedio es %f segs" % resolutionTime.mean())
    print("")

#
# Hago las pruebas de cada caso
#   
p = 0.6
q = 1 - p
    
lambdaA1 = 1.0/4.0
muA1 = 1.0/0.7
capacidad_servidor(_lambda=lambdaA1,_mu=muA1, _arrives=int(arrives*p))

lambdaA2 = 1.0/4.0
muA2 = 1.0/1.0
capacidad_servidor(_lambda=lambdaA2,_mu=muA2, _arrives=int(arrives*q))

lambdaB = 1.0/4.0
muB = 1.0/0.8
capacidad_servidor(_lambda=lambdaB,_mu=muB, _arrives=int(arrives))

"""
FIN punto 1

"""
