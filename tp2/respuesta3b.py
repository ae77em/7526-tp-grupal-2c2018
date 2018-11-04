"""
Punto 3b

"""
from scipy.integrate import odeint
from scipy import arange
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure
from matplotlib.pyplot import show
import sympy

def f(x,y):
    return x * 0.5 + y

def g(x, y):
    return y - x * 0.5

def h(x,y,z):
    return z - (x + y)

def crazy_recurrence_function(state0, t):
    x = state0[0]
    y = state0[1]
    z = state0[2]
    
    xd = f(x, y)
    yd = g(x, y)
    zd = h(x, y ,z)

    return [xd, yd, zd]


number_of_iterations = 100
fig = figure()
ax = fig.gca(projection='3d')

linestyles = ['->', '-->', '-.>', ':>']
l=0

for i in [-1, 0, -1]:
    for j in [-1, 0, -1]:
        for k in [-1, 0, -1]:
            state0 = [i, j, k]
            
            t = arange(0, number_of_iterations, 1)

            state = odeint(crazy_recurrence_function, state0, t)
            
            ax.plot(state[:,0],state[:,1],state[:,2], linestyles[l], label='Estado inicial '+ str(state0), linewidth=l+1)
            ax.legend()
            l += 1
            if l>3:
                l = 0

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

show()

"""
FIN punto 3b

"""
