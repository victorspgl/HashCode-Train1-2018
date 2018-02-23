# Programa principal
# Victor Soria Pardos
# 7 Febrero 2018

from problema import Problema
from problema import Configuracion
from problema import puntuacionReal

from read import lectura_problema
from search import hill_climbing
from read import almacenar_solucion

# define la función

def mcd(a, b):
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

while True:
    nombre_fichero = input("Introduce fichero de entrada: ")

    configuracion = lectura_problema(nombre_fichero)

    x = configuracion.getDimensionx()
    y = configuracion.getDimensiony()
    divisor = mcd(x, y)


    if divisor < 10 :
        problema = Problema(subConfiguracion)

        nodoMejor = hill_climbing(problema)
        print(puntuacionReal(nodoMejor))
        while puntuacionReal(nodoMejor) <= 0:
            nodoNuevo = hill_climbing(problema)
            if puntuacionReal(nodoNuevo) > puntuacionReal(nodoMejor):
                print(puntuacionReal(nodoNuevo))
                nodoMejor = nodoNuevo

        almacenar_solucion(nodoMejor)

    else:

        divisor = 10

        num = configuracion.getSize() / divisor*divisor

        solucion = []

        for i in range(0, int(num)):

            subConfiguracion = Configuracion()

            subConfiguracion.setParametrosIniciales(divisor, divisor, configuracion.getMinimo(), configuracion.getMaximo())

            array = configuracion.getArray()

            for j in range(0, divisor):
                for k in range(0, divisor):
                    subConfiguracion.setAtributo(j,k,array[j + i*divisor, k + i*divisor])


            problema = Problema(subConfiguracion)

            nodoMejor = hill_climbing(problema)
            print(puntuacionReal(nodoMejor))
            while puntuacionReal(nodoMejor) <= 0:
                nodoNuevo = hill_climbing(problema)
                if puntuacionReal(nodoNuevo) > puntuacionReal(nodoMejor):
                    print(puntuacionReal(nodoNuevo))
                    nodoMejor = nodoNuevo

            lonchas = nodoMejor.getLonchas()
            for l in range(0, nodoMejor.getNumLonchas):
                solucion = solucion.append(lonchas[l])



        almacenar_solucion(solucion)

