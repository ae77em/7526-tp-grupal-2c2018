def generador_congruencial_lineal(x_n):
    m = 232                     # modulus
    a = 1013904223              # multiplier
    c = 1664525                 # increment

    x = float(((a * x_n) + c) % m) / float(m)

    return x
