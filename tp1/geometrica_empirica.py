from generador_congruencial_lineal import generador_congruencial_lineal

def experimento_geometrica(p):
    # genero numero aleatorios uniformes
    x_n = (90697 + 89563) // 2
    empiricos = []

    # hago el experimento
    for _ in range(10000):
        salio1 = False
        while not salio1:
            x_n = generador_congruencial_lineal(x_n)

            if (x_n >= 0.0 and x_n < 1-p):
                empiricos.append(0)
            else:
                empiricos.append(1)
                salio1 = True

    return empiricos