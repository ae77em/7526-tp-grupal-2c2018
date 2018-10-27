# RESPUESTA 1 paso 1
import constante

def gcl(x_n):
   m = 232                     # modulus
   a = 1013904223              # multiplier
   c = 1664525                 # increment

   x = ((a * x_n) + c) % m

   return x

x_n = constante.SEMILLA

for _ in range(6):
   x_n = gcl(x_n)
   print(x_n)
