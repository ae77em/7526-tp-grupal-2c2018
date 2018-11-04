import sympy
    
x, y, z = sympy.symbols('x, y, z', negative=False)
X = x * 0.5 + y
Y = y - x * 0.5
Z = z - (x + y)

# use sympy's way of setting equations to zero
XEqual = sympy.Eq(X, 0)
YEqual = sympy.Eq(Y, 0)
ZEqual = sympy.Eq(Z, 0)

# compute fixed points
equilibria = sympy.solve( (XEqual, YEqual, ZEqual), x, y, z )
print("Puntos de equilibrio")
print(equilibria)
