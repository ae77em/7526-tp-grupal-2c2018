def generador_congruencial_lineal(x_n, k=0):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c - k*m) % m) / float(m)

    return x
