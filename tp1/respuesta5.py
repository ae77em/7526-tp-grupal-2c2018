from funciones import generador_congruencial_lineal
import constante

# genero numero aleatorios uniformes
x_n = constante.SEMILLA
uniformes = []
empiricos = []

for _ in range(constante.CANT_EXPERIMENTOS):
    x_n = generador_congruencial_lineal(x_n)
    uniformes.append(x_n)

# la funcion definida por la tabla en el enunciado es:
# f(x) = I{ 0 <= x < 0.5}  + 2 * I{ 0.5 <= x < 0.7} + 3 * I{ 0.7 <= x < 0.8} + 4 * I{ 0.8 <= x < 1}
# Luego:
for nro in uniformes:
    if (nro >= 0 and nro < 0.5):
        empiricos.append(1)
    elif (nro >= 0.5 and nro < 0.7):
        empiricos.append(2)
    elif (nro >= 0.7 and nro < 0.8):
        empiricos.append(3)
    else:
        empiricos.append(4)

print(empiricos)