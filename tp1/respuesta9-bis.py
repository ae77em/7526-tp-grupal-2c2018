import scipy.stats as stats

import constante
from funciones import gcl_uniforme

def gap_test(alfa=0, beta=1):
    gaps = [0] * constante.CANT_EXPERIMENTOS
    i=0
    gap=0
    x_n = gcl_uniforme(constante.SEMILLA)

    while (i < constante.CANT_EXPERIMENTOS):
        if ((x_n < alfa) or (x_n >= beta)):
            gap += 1                 
        else:
            gaps[i] = gap + 1
            i += 1
            gap = 0
        
        x_n = gcl_uniforme(x_n)

    p = beta - alfa
    gapMax = max(gaps)

    # agrupo en 11 clases (de la 0 a la 10)
    observed = [0] * 11
    for i in range(10):
        observed[i] = gaps.count(i+1)

    for i in range(10, gapMax+1):
        observed[10] += gaps.count(i)

    expected = [0] * 11
    for i in range(10):
        expected[i] = p * ((1-p)**(i)) * constante.CANT_EXPERIMENTOS

    for i in range(10, gapMax+1):
        expected[10] += p * ((1-p)**(i-1)) * constante.CANT_EXPERIMENTOS

    print("observed", observed)
    print("expected", expected)

    Dsquared, p = stats.chisquare(observed, f_exp=expected)

    t = stats.chi2.ppf(q=0.95, df=10)

    print ("Aplicamos test chi cuadrado a los resultados de test gap.")
    print ("t: " + str(t))
    print ("D^2 : " + str(Dsquared))

    if (Dsquared < t):
        print("ACEPTAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(alfa, beta))
    else:
        print("RECHAZAMOS la hipotesis con un error del 5% para el gap test con intervalo [{0}, {1}].".format(alfa, beta))


gap_test(0.5, 1)
gap_test(0.2, 0.6)
    
