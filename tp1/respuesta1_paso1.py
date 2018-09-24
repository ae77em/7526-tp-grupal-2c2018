'''
Ejercicio 1
Utilizando Matlab, Octave o Python implementar un Generador Congruencial Lineal (GCL) de modulo 232, multiplicador
1013904223, incremento de 1664525 y semilla igual a la parte entera del promedio de los numeros de padron de los
integrantes del grupo.
 * Informar los primeros 6 numeros al azar de la secuencia.
 * Modificar el GCL para que devuelva numeros al azar entre 0 y 1, y realizar un histograma sobre 100.000 valores generados.
'''
def generador_congruencial_lineal(x_n):
   m = 232                     # modulus
   a = 1013904223              # multiplier
   c = 1664525                 # increment

   x = ((a * x_n) + c) % m

   return x

x_n = (90697 + 89563) // 2

for _ in range(6):
   x_n = generador_congruencial_lineal(x_n)
   print(x_n)