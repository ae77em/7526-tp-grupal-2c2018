"""
Punto 1

"""
import numpy
import random
import matplotlib.pylab as plt

arrives = 100

def computeQueue(arrivals, systemCapacity): 
    N = len(arrivals)
    Q = numpy.zeros(N,dtype=int) # make a list to store the values of  Q
    d = numpy.zeros(N,dtype=int) # make a list to store the values of  d
    Q[0] = 0 #  initial queue length is 0
    for n in range(1,N):
        d[n] = min( Q[n-1] + arrivals[n], systemCapacity[n])
        Q[n] = Q[n-1] + arrivals[n] - d[n]
    
    return Q, d

def waitingTime(arrivals,departures):
    # At[i] is the number of arrivals in time slot i
    # Convert this to the arrival time of each customer
    arrivalTimes = numpy.repeat(numpy.arange(len(arrivals)), arrivals)
    # Dt[i] is the number of departures in time slot i
    # Convert this to the departure time of each customer
    departureTimes = numpy.repeat(numpy.arange(len(departures)), departures)
    m = min(len(arrivalTimes), len(departureTimes))
    waits = departureTimes[:m] - arrivalTimes[:m]
    
    return waits

def baseAttention(_lambda=1, _mu=1, _arrives=100000):
    baseArrivals = numpy.random.poisson(_lambda, size=int(_arrives))
    baseCapacity = _mu*numpy.ones_like(baseArrivals)

    queueSizes, departures = computeQueue(baseArrivals, baseCapacity)
       
    baseWaitingTime = waitingTime(baseArrivals, departures)
    
    print("El tiempo medio de espera es de %f segs" % baseWaitingTime.mean())
    aux = float(queueSizes.tolist().count(0)) / float(_arrives) * 100
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
baseAttention(_lambda=lambdaA1,_mu=muA1, _arrives=int(arrives*p))

lambdaA2 = 1.0/4.0
muA2 = 1.0/1.0
baseAttention(_lambda=lambdaA2,_mu=muA2, _arrives=int(arrives*q))

lambdaB = 1.0/4.0
muB = 1.0/0.8
baseAttention(_lambda=lambdaB,_mu=muB, _arrives=int(arrives))

"""
FIN punto 1

"""
