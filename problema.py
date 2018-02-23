# Clase descripcion de problema
# Victor Soria Pardos
# 7 Febrero 2018

import copy
import numpy as np
from search import Problem
from search import Node

class Configuracion(object):

    def setParametrosIniciales(self, dimensionx, dimensiony, minimoIngredientes, maximoRodajas):
        if dimensionx < 1 or dimensionx > 1000 :
            "error"
        if dimensiony < 1 or dimensiony > 1000 :
            "error"
        if minimoIngredientes < 1 or minimoIngredientes > 1000 :
            "error"
        if maximoRodajas < 1 or maximoRodajas > 1000 :
            "error"

        self.x = dimensionx
        self.y = dimensiony
        self.minimo = minimoIngredientes
        self.maximo = maximoRodajas
        self.array = np.zeros((self.x, self.y),dtype=np.uint8)
        self.ocupado = np.zeros((self.x, self.y),dtype=np.uint8)
        self.numLonchas = 0
        self.lonchas = []

    def getArray(self):
        return self.array

    def getDimensionx(self):
        return self.x

    def getDimensiony(self):
        return self.y

    def getSize(self):
        return self.x * self.y

    def getMinimo(self):
        return self.minimo

    def getMaximo(self):
        return self.maximo

    def setAtributo(self, i, j, x):
        if isinstance(x, str):
            if x == 'M':
                self.array[i, j] = 0
            elif x == 'T':
                self.array[i, j] = 1
        else:
            if x == 0:
                self.array[i, j] = 0
            elif x == 1:
                self.array[i, j] = 1


    def getOcupados(self):
        return self.ocupado

    def getNumLonchas(self):
        return self.numLonchas

    def getLonchas(self):
        return self.lonchas

    def addLoncha(self,xinit,yinit):
        if(xinit >= 0 and xinit < self.x and yinit >= 0 and yinit < self.y and self.ocupado[xinit,yinit] == 0):
            self.numLonchas = self.numLonchas + 1
            self.lonchas.append([xinit,yinit,xinit,yinit])
            self.ocupado[xinit,yinit] = 1

    def growLoncha(self,numLoncha,direccion):
        if(numLoncha < self.numLonchas):
            if direccion == 0 and self.lonchas[numLoncha][2] < (self.x - 1) and self.compruebax(self.lonchas[numLoncha],1):
                self.ocupar(self.lonchas[numLoncha][2] + 1, self.lonchas[numLoncha][2] + 1, self.lonchas[numLoncha][1], self.lonchas[numLoncha][3])
                self.lonchas[numLoncha][2] = self.lonchas[numLoncha][2] + 1

            elif direccion == 1 and self.lonchas[numLoncha][3] < (self.y - 1) and self.compruebay(self.lonchas[numLoncha],1):
                self.ocupar(self.lonchas[numLoncha][0], self.lonchas[numLoncha][2], self.lonchas[numLoncha][3] + 1, self.lonchas[numLoncha][3] + 1)
                self.lonchas[numLoncha][3] = self.lonchas[numLoncha][3] + 1


            elif direccion == 2 and self.lonchas[numLoncha][2] > 0 and self.compruebax(self.lonchas[numLoncha],-1):
                self.ocupar(self.lonchas[numLoncha][2] - 1, self.lonchas[numLoncha][2] - 1, self.lonchas[numLoncha][1], self.lonchas[numLoncha][3])
                self.lonchas[numLoncha][2] = self.lonchas[numLoncha][2] - 1

            elif direccion == 3 and self.lonchas[numLoncha][3] > 0 and self.compruebay(self.lonchas[numLoncha],-1):
                self.ocupar(self.lonchas[numLoncha][0], self.lonchas[numLoncha][2], self.lonchas[numLoncha][3] - 1, self.lonchas[numLoncha][3] - 1)
                self.lonchas[numLoncha][3] = self.lonchas[numLoncha][3] - 1

    def do(self,action):
        if(action[0] == 0):
            self.addLoncha(action[1],action[2])
        elif(action[0] == 1):
            self.growLoncha(action[1],action[2])

    def compruebax(self,loncha,add):
        anchura = abs(loncha[1] - loncha[3])
        minimo = min(loncha[1],loncha[3])
        ok = True
        for i in range(0,anchura+1):
            ok = ok and (self.ocupado[loncha[2] + add][minimo + i] == 0)
        return ok

    def compruebay(self,loncha,add):
        anchura = abs(loncha[0] - loncha[2])
        minimo = min(loncha[0],loncha[2])
        ok = True
        for i in range(0,anchura+1):
            ok = ok and (self.ocupado[minimo + i][loncha[3] + add] == 0)
        return ok

    def operable(self,numLoncha,direccion):
        if(numLoncha < self.numLonchas):
            if direccion == 0 and self.lonchas[numLoncha][2] < (self.x - 1) and self.compruebax(self.lonchas[numLoncha],1):
                return True

            elif direccion == 1 and self.lonchas[numLoncha][3] < (self.y - 1) and self.compruebay(self.lonchas[numLoncha],1):
                return True

            elif direccion == 2 and self.lonchas[numLoncha][2] > 0 and self.compruebax(self.lonchas[numLoncha],-1):
                return True

            elif direccion == 3 and self.lonchas[numLoncha][3] > 0 and self.compruebay(self.lonchas[numLoncha],-1):
                return True

            else:
                return False

    def ocupar(self, coordxi, coordxf, coordyi, coordyf):
        if coordxi != min(coordxi, coordxf):
            aux = coordxi
            coordxi = coordxf
            coordxf = aux
        if coordyi != min(coordyi, coordyf):
            aux = coordyi
            coordyi = coordyf
            coordyf = aux
        for x in range(coordxi, coordxf+1):
            for y in range(coordyi, coordyf+1):
                self.ocupado[x,y] = self.ocupado[x,y] + 1


class Problema(Problem):

    def __init__(self,configuracion):
        self.initial = configuracion
        self.goal = None

    def actions(self, state):
        ocupados = state.getOcupados()
        acciones = []
        for i in range(0,state.getNumLonchas()):
            for j in range(0,4):
                if state.operable(i,j) :
                    acciones.append([1,i,j])
        for i in range(0, state.getDimensionx()):
            for j in range(0, state.getDimensiony()):
                if ocupados[i][j] == 0 :
                    acciones.append([0,i,j])
        return acciones

    def result(self, state, action):
        nuevo_estado = copy.deepcopy(state)
        nuevo_estado.do(action)
        return nuevo_estado

    def value(self, state):
        configuracion = state
        numLonchas = configuracion.getNumLonchas()
        lonchas = configuracion.getLonchas()
        ocupados = configuracion.getOcupados()
        array = configuracion.getArray()
        numMinimo = configuracion.getMinimo()
        numMaximo = configuracion.getMaximo()

        sum = 0
        for i in range(0,numLonchas):
            loncha = lonchas[i]
            anchura = abs(loncha[0] - loncha[2]) + 1
            minimox = min(loncha[0], loncha[2])
            altura = abs(loncha[1] - loncha[3]) + 1
            minimoy = min(loncha[1], loncha[3])
            sumLoncha = 0
            numTomate = 0
            numSeta = 0
            error = 0
            for j in range(minimox,anchura + minimox ):
                for k in range(minimoy, altura + minimoy ):
                    if (ocupados[j,k] > 1.0):
                        error = 2

                    if array[j,k] == 0:
                        numSeta = numSeta + 1
                    else:
                        numTomate = numTomate + 1

                    sumLoncha = sumLoncha + 1;

            if error < 1 and (numTomate < numMinimo or  numSeta < numMinimo) :
                error = 1

            if sumLoncha > numMaximo:
                error = 2

            if error == 1 :
                sum = sum + sumLoncha * sumLoncha
            elif error == 0:
                sum = sum + sumLoncha * sumLoncha * sumLoncha
            elif error == 2:
                return 0

        return sum

def puntuacionReal(nodo):
    configuracion = nodo
    numLonchas = configuracion.getNumLonchas()
    lonchas = configuracion.getLonchas()
    ocupados = configuracion.getOcupados()
    array = configuracion.getArray()
    numMinimo = configuracion.getMinimo()
    numMaximo = configuracion.getMaximo()

    sum = 0
    for i in range(0, numLonchas):
        loncha = lonchas[i]
        anchura = abs(loncha[0] - loncha[2]) + 1
        minimox = min(loncha[0], loncha[2])
        altura = abs(loncha[1] - loncha[3]) + 1
        minimoy = min(loncha[1], loncha[3])
        sumLoncha = 0
        numTomate = 0
        numSeta = 0
        error = 0
        for j in range(minimox, anchura + minimox):
            for k in range(minimoy, altura + minimoy):
                if (ocupados[j, k] > 1.0):
                    error = 2

                if array[j, k] == 0:
                    numSeta = numSeta + 1
                else:
                    numTomate = numTomate + 1

                sumLoncha = sumLoncha + 1;

        if error < 1 and (numTomate < numMinimo or numSeta < numMinimo):
            error = 1

        if sumLoncha > numMaximo:
            error = 2

        if error == 1:
            return 0
        elif error == 0:
            sum = sum + sumLoncha
        elif error == 2:
            return 0

    return sum
