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