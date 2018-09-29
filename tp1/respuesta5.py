'''
Utilizando el metodo de la transformada inversa y utilizando el generador de numeros aleatorios implementado en el
ejercicio 1 genere numeros aleatorios siguiendo la siguiente funcion de distribucion de probabilidad empirica.

Probabilidad    Valor generado
    .5              1
    .2              2
    .1              3
    .2              5

'''

## funciones auxiliares
def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x

# genero numero aleatorios uniformes
x_n = (90697 + 89563) // 2
uniformes = []
empiricos = []

for _ in range(100000):
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