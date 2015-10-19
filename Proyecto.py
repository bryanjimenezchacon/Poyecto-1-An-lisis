from random import randint

from abc import *
import copy
import string
## Ejemplo de uso "mincover.txt  datos.txt       100          1000          3            2         output.txt"
##                nombre_prob/ nombre_archi/ #generaciones/ tam_pobla* / %mutacion/ tipo_selec**/ archi_out
##
## *Si tam_pobla = 0 ignorar y leer del archivo, sino hay hacer random
## ** 0 = simple al azar, 1 = rueda de la fortuna, 2 torneo,
##  si utiliza cruce simple al azar (0) su algoritmo debe ser de punto fijo


#######################################################################################################################
## Revisar que recubrimiento <= cant_vertices

#######################################################################################################################
class Problema():
    """ Clase que lee un archivo de texto con el problema
    """
    def readProblema(self, archivo ):## Leer el problema del archivo
            self.archivo = archivo

    def geneSize(self):## Retorna el tamanio del gen
        self.tamano = tamano
        tamano = len(m_genes[0])
        return tamano

    def fitness(self, gen):## Calculo del fitness
        self.gen = gen
        pass

    def name(self, nombre):## Retorna el nombre del problema
        self.nombre = nombre
        return nombre
        pass

##########################################-----VERTEX-----##########################################
class Vertex(Problema):

        def __init__(self, politica, numCruces, mutacion, tamPoblacion, cantGeneraciones):
                     self.politica = politica
                     self.numCruces = numCruces
                     self.mutacion = mutacion
                     self.tamPoblacion = tamPoblacion
                     self.matrizConexiones = []
                     self.cantGeneraciones = cantGeneraciones
                     self.matrizPoblacion = []
                     
        def readProblema(self):
               
                self.archi = open("problemaVertex.txt" , 'r')
                self.nombre = self.archi.readline()#Nombre del problema
                self.numVertices = int(self.archi.readline())
                self.numAristas = int(self.archi.readline())
                self.tamanioRecubrimiento = int(self.archi.readline())
                
                self.linea = self.archi.readline()
                while self.linea != "":
                    
                  # print (self.linea)
                    self.matrizConexiones.append([int(self.linea[0]), int(self.linea[1])])
                  #  print(self.matrizConexiones)
                    self.linea = self.archi.readline()
                    
                self.archi.close()

        def geneSize(self):

                self.datos = open("datosVertex.txt", 'r')
                self.datos.readline() #nombre
                self.datos.readline() #tamanio Poblacion
                
                self.primerGen = self.datos.readline()
                self.tamanioGen = len(self.primerGen) - 1
        
                return self.tamanioGen

        def fitness(self,gen):
                print("Matriz Conexiones: " + str(self.matrizConexiones))
                 
                self.gen = gen
                self.num_ceros = 0

                self.AristasNoCubiertas = copy.deepcopy(self.matrizConexiones)
                ##print("Aristas No Cubiertas Antes  : " + str(self.AristasNoCubiertas))
                for i in range(len(self.gen)):#Calcular numero de unos y ceros
                        if self.gen[i] == 0:
                                self.num_ceros += 1

                self.num_unos = self.geneSize() - self.num_ceros
                print("Numeros de unos: " + str(self.num_unos))
                listaIndices = []
                listaIndicesFinal = []
                
                self.AristasNoCubiertas = copy.deepcopy(self.matrizConexiones)
                
                for j in range(len(gen)):#Busca los indices de la matriz que debe eliminar
                        if gen[j] == 1:
                                for i in range(len(x.matrizConexiones)):
                                        if (j+1) in x.matrizConexiones[i]:
                                                listaIndices.append(i)
                                                
                for i in listaIndices:  #Limpia las lista si hay repetidos
                        if i not in listaIndicesFinal:
                                listaIndicesFinal.append(i)
                                
                listaIndicesFinal.sort()
                listaIndicesFinal.reverse()
                print("Lista de Indices Final: " + str(listaIndicesFinal))
                
                for i in range(len(listaIndicesFinal)): #Elimina las aristas
                        self.AristasNoCubiertas.remove(self.AristasNoCubiertas[listaIndicesFinal[i]])

                print("Aristas no cubiertas despuÃ©s: " + str(self.AristasNoCubiertas))

                self.cantidadAristasNoCubiertas = len(self.AristasNoCubiertas)
                
                self.fitnessFinal = self.num_ceros * ((self.num_unos + 1) - self.cantidadAristasNoCubiertas)

                return self.fitnessFinal

        def name():
                return self.nombre
                                                            
        def resetPoblacion(self, tamano):
                self.matrizRes = []
                for j in range(0, tamPoblacion):
                    for i in range(0, P.geneSize()):
                        self.vectorDeMatriz = []
                        self.numero = random.randint(0,1)
                        self.vectorDeMatriz.append(numero)

        def readPoblacion(self):
                self.datos = open("datosVertex.txt", 'r')
                
                self.matrizPoblacion = [] #Matriz final en donde quedará guardada la población
                self.listaGen = [] #Lista auxiliar para ciclo
                saltoLinea = 0 #Variable para indicar el comienzo de la población en archivo

                for line in self.datos:
                        if saltoLinea > 1:
                                if line[-1] != "\n":
                                        for i in range(len(line)):
                                                self.listaGen.append(int(line[i]))
                                                
                                        self.matrizPoblacion.append(copy.deepcopy(self.listaGen))
                                        
                                        del self.listaGen[:] # Elimina todos los elementos de la lista
                                        self.listaGen[:] = []
                                        
                                else:
                                        
                                        for i in range(len(line) - 1):
                                                self.listaGen.append(int(line[i]))
                                                
                                        self.matrizPoblacion.append(copy.deepcopy(self.listaGen))
                                        
                                        del self.listaGen[:] # Elimina todos los elementos de la lista
                                        self.listaGen[:] = []
                                
                                
                        elif saltoLinea == 1:
                                self.tamPoblacion = int(line[:-1])
                                saltoLinea += 1
                        else:
                                saltoLinea += 1
    
        def writePoblacion(self):
                self.stringPoblacion = ""
                
                for i in range(len(self.matrizPoblacion)):
                        for j in range(len(self.matrizPoblacion[i])):
                                self.stringPoblacion += (str(self.matrizPoblacion[i][j]))
                                        
                        self.stringPoblacion += "\n"
                self.salida = open("output.txt", 'w')
                self.salida.write("GT1\n" + str(self.tamPoblacion) + "\n" + self.stringPoblacion)
                self.salida.close()
                
        def generacion(self):
                pass
    
        def getBest(self):
            listaResulFitness = []
            for i in range(len(self.matrizPoblacion)):
                listaResulFitness.append(self.fitness(self.matrizPoblacion[i]))
            print(listaResulFitness)
            print("El mejor es : " + str(self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]))
            return self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]

        def seleccionarGen():

            if self.politica == 0: # Simple al azar
                self.filaRandomPrimerGen = randint(0, len(self.matrizPoblacion) - 1)
                self.columnaRandomPrimerGen = randint(0, len(self.matrizPoblacion[0]) - 1)

                self.filaRandomSegundoGen = randint(0, len(self.matrizPoblacion) - 1)
                self.columnaRandomSegundoGen = randint(0, len(self.matrizPoblacion[0]) - 1)

                if self.filaRandomPrimerGen == self.filaRandomSegundoGen and self.columnaRandomPrimerGen == self.columnaRandomSegundoGen:
                       seleccionarGen()

                self.GenPadre = self.matrizPoblacion[self.filaRandomPrimerGen][self.columnaRandomPrimerGen]
                self.GenMadre = self.matrizPoblacion[self.filaRandomSegundoGen][self.columnaRandonSegundoGen]

                #Falta verificar que el numero de puntos no sea mayor al tama�o del gen

                self.listaPuntosFijos = []

                for i in range(self.numCruces):
                    self.indiceRandom = randint(0, self.geneSize() - 1)
                    self.listaPuntosFijos.append(self.indiceRandom)
                    
                for i in range(len(self.listaPuntosFijos)):
                    if i != len(self.listaPuntosFijos) - 1:
                        if listaPuntosFijos[i] == listaPuntosFijos[i+1]:
                            seleccionarGen()
                            
                self.lsitaPuntosFijos.sort()
                self.listaPuntosFijos.append(geneSize())

                self.Hijo_A = []
                self.Hijo_B = []

                estaArriba = true
                contadorIndices = 0
                
                for i in range(len(self.listaPuntosFijos)):
                    while contadorIndices != self.listaPuntosFijos[i]:
                        if estaArriba:
                            self.Hijo_A.append(self.GenPadre[contadorIndices])
                            self.Hijo_B.append(self.GenMadre[contadorIndices])
                            estaArriba = false
                        else:
                            self.Hijo_A.append(self.GenMadre[contadorIndices])
                            self.Hijo_B.append(self.GenPadre[contadorIndices])
                            estaArriba = true
                        contadorIndices += 1
    
            elif self.politica == 1: # Rueda de la fortuna
                pass

            else: # Torneo
                pass



#Falta verificar que la población sea válida con el tamaño de recubrimiento
#Falta hacer la restricción en caso de que el tamaño de población sea cero 

##########################################-----MIN COVER-----##########################################
class Recubrimiento(Problema):

        def __init__(self, politica, numCruces, mutacion, tamPoblacion, cantGeneraciones):
                     self.politica = politica
                     self.numCruces = numCruces
                     self.mutacion = mutacion
                     self.tamPoblacion = tamPoblacion
                     self.subconjuntos = []
                     self.cantGeneraciones = cantGeneraciones
                     self.matrizPoblacion = []
##    def resetPoblacion(self, tamano):
##        pass
##
        def readProblema(self):
               
                self.archi = open("problemaRec.txt" , 'r')
                self.nombre = self.archi.readline()#Nombre del problema
                self.tamUniverso = int(self.archi.readline())
                self.cantSubconjuntos = int(self.archi.readline())
                
                self.linea = self.archi.readline()
                while self.linea != "":
                    listaSubconjunto = []
                    for i in range(len(self.linea)):
                        if self.linea[i] == '\n':
                            pass
                        else:
                            listaSubconjunto.append(int(self.linea[i]))
                    self.subconjuntos.append(listaSubconjunto)
                    self.linea = self.archi.readline()
                print(self.subconjuntos)
                self.archi.close()

        def readPoblacion(self):
                self.datos = open("datosRecMin.txt", 'r')
                
                self.matrizPoblacion = [] #Matriz final en donde quedará guardada la población
                self.listaGen = [] #Lista auxiliar para ciclo
                saltoLinea = 0 #Variable para indicar el comienzo de la población en archivo

                for line in self.datos:
                        if saltoLinea > 1:
                                if line[-1] != "\n":
                                        for i in range(len(line)):
                                                self.listaGen.append(int(line[i]))
                                                
                                        self.matrizPoblacion.append(copy.deepcopy(self.listaGen))
                                        
                                        del self.listaGen[:] # Elimina todos los elementos de la lista
                                        self.listaGen[:] = []
                                        
                                else:
                                        
                                        for i in range(len(line) - 1):
                                                self.listaGen.append(int(line[i]))
                                                
                                        self.matrizPoblacion.append(copy.deepcopy(self.listaGen))
                                        
                                        del self.listaGen[:] # Elimina todos los elementos de la lista
                                        self.listaGen[:] = []
                                
                                
                        elif saltoLinea == 1:
                                self.tamPoblacion = int(line[:-1])
                                saltoLinea += 1
                        else:
                                saltoLinea += 1
        def writePoblacion(self):
                self.stringPoblacion = ""
                
                for i in range(len(self.matrizPoblacion)):
                        for j in range(len(self.matrizPoblacion[i])):
                                self.stringPoblacion += (str(self.matrizPoblacion[i][j]))
                                        
                        self.stringPoblacion += "\n"
                self.salida = open("output.txt", 'w')
                self.salida.write("SP5\n" + str(self.tamPoblacion) + "\n" + self.stringPoblacion)
                self.salida.close()

        def fitness(self, gen):
            pass

        def generacion(self):
            pass
##
##    def getBest(self, gen=None):
##        self.gen = gen
##        return gen
##        pass
###############################################-----PROGRAMA-----###############################################

def main():

    stringInstrucciones = "genetico mincover.txt datosVertex.txt 100 1000 3 2 output.txt"
    listaInstrucciones = stringInstrucciones.split()
    print(listaInstrucciones)

    pCantGeneraciones = int(listaInstrucciones[3])
    pTamPoblacion = int(listaInstrucciones[4])
    pMutacion = int(listaInstrucciones[5])
    pPolitica = int(listaInstrucciones[6])

    #
    numeroDeCruces = 2
    #
    y = [1,1,1,0,1]
    x = Vertex(pPolitica, numeroDeCruces, pMutacion, pTamPoblacion, pCantGeneraciones)
    x.readPoblacion()
    x.readProblema()

    genElegido = x.seleccionarGen()


    x.fitness(y)
    print("\nRECUBRIMIENTO\n" )
    r = Recubrimiento(pPolitica, numeroDeCruces, pMutacion, pTamPoblacion,  pCantGeneraciones)
    r.readProblema()
    r.readPoblacion()
    
if __name__ == "__main__":
    main()
