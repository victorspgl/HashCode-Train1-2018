# Lector de ficheros de descripcion de problema
# Victor Soria Pardos
# 7 Febrero 2018

from problema import Configuracion

def lectura_problema(nombreFichero):
    fichero_objeto = open(nombreFichero, "r")
    lineas = fichero_objeto.readlines()

    config = Configuracion()
    filas, columnas, min, max = [int(i) for i in lineas[0].split(' ')]

    config.setParametrosIniciales(filas, columnas, min, max)
    for i in range(0,config.getDimensionx()):
        for j in range(0,config.getDimensiony()):
            config.setAtributo(i, j, lineas[i+1][j])
    return config


def almacenar_solucion(solucion):
    fichero_objeto = open("solucion.txt", "w")
    num = solucion.getNumLonchas()
    fichero_objeto.write(str(num) + "\n")
    lonchas = solucion.getLonchas()
    for i in range(0, num):
        fichero_objeto.write(str(lonchas[i]).strip("[]").replace(",",""))
        fichero_objeto.write("\n")
    fichero_objeto.close()
