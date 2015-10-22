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
        self.tamano = len(m_genes[0])
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
                     self.nuevaPoblacion = []
                     self.nombre = "GT1"
                    
                     
        def readProblema(self):
            self.archi = open("problemaVertex.txt" , 'r')
            self.nombre = self.archi.readline()#Nombre del problema

            self.cantidadesEspecificas = self.archi.readline().replace("\n", "")
            
            listaCantidadesConvertidas = self.cantidadesEspecificas.split()

            for i in range(len(listaCantidadesConvertidas)):
                listaCantidadesConvertidas[i] = int(listaCantidadesConvertidas[i])
            
            self.numVertices = listaCantidadesConvertidas[0]
            self.numAristas = listaCantidadesConvertidas[1]
            self.tamanioRecubrimiento = listaCantidadesConvertidas[2]
            
            self.linea = self.archi.readline()
            while self.linea != "":
                vectorAuxiliar = self.linea.replace("\n", "")
                vectorAuxiliar = vectorAuxiliar.split()
              # print (self.linea)
                self.matrizConexiones.append([int(vectorAuxiliar[0]), int(vectorAuxiliar[1])])
              #  print(self.matrizConexiones)
                self.linea = self.archi.readline()
                
            self.archi.close()

        def geneSize(self):

                self.datos = open("gt1.txt", 'r')
                self.datos.readline() #nombre
                datosPrincipales = self.datos.readline()
                datosPrincipales = datosPrincipales.split()
                self.tamanioGen = int(datosPrincipales[0])
                
                return self.tamanioGen

        def fitness(self,gen):
               # print("Matriz Conexiones: " + str(self.matrizConexiones))
                 
                self.gen = gen
                self.num_ceros = 0

                self.AristasNoCubiertas = copy.deepcopy(self.matrizConexiones)
                ##print("Aristas No Cubiertas Antes  : " + str(self.AristasNoCubiertas))
                for i in range(len(self.gen)):#Calcular numero de unos y ceros
                        if self.gen[i] == 0:
                                self.num_ceros += 1

                self.num_unos = self.geneSize() - self.num_ceros
                #print("Numeros de unos: " + str(self.num_unos))
                listaIndices = []
                listaIndicesFinal = []
                
                self.AristasNoCubiertas = copy.deepcopy(self.matrizConexiones)
                
                for j in range(len(gen)):#Busca los indices de la matriz que debe eliminar
                        if gen[j] == 1:
                                for i in range(len(self.matrizConexiones)):
                                        if (j+1) in self.matrizConexiones[i]:
                                                listaIndices.append(i)
                                                
                for i in listaIndices:  #Limpia las lista si hay repetidos
                        if i not in listaIndicesFinal:
                                listaIndicesFinal.append(i)
                                
                listaIndicesFinal.sort()
                listaIndicesFinal.reverse()
              #  print("Lista de Indices Final: " + str(listaIndicesFinal))
                
                for i in range(len(listaIndicesFinal)): #Elimina las aristas
                        self.AristasNoCubiertas.remove(self.AristasNoCubiertas[listaIndicesFinal[i]])

               # print("Aristas no cubiertas despuÃƒÆ’Ã‚Â©s: " + str(self.AristasNoCubiertas))

                self.cantidadAristasNoCubiertas = len(self.AristasNoCubiertas)
                
                self.fitnessFinal = self.num_ceros * ((self.num_unos + 1) - self.cantidadAristasNoCubiertas)

                return self.fitnessFinal

        def name(self):
                return self.nombre
                                                            
        def resetPoblacion(self):

            matrizNuevaPoblacion = []
            
            for i in range(0, self.tamPoblacion):
                    listaAux = []
                    for j in range(0, self.geneSize()):
                        listaAux.append(randint(0,1))
                    matrizNuevaPoblacion.append(listaAux)

            
            self.archi = open("datosVertex.txt", "w")
            self.archi.write(str(self.tamPoblacion) + "\n")

            for i in range(len(matrizNuevaPoblacion)):
                for j in range(len(matrizNuevaPoblacion[i])):
                    self.archi.write(str(matrizNuevaPoblacion[i][j]))

                self.archi.write("\n")

            self.archi.close()    

        def readPoblacion(self):
                self.datos = open("datosVertex.txt", 'r')
                
                self.matrizPoblacion = [] #Matriz final en donde quedarÃƒÂ¡ guardada la poblaciÃƒÂ³n

                if self.tamPoblacion == 0:
                    self.listaGen = [] #Lista auxiliar para ciclo
                    saltoLinea = 0 #Variable para indicar el comienzo de la poblaciÃƒÂ³n en archivo
                    
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

                else:
                    for i in range(self.tamPoblacion):
                        listaAux = []
                        for j in range(self.geneSize()):
                            listaAux.append(randint(0,1))
                        self.matrizPoblacion.append(listaAux)
    
        def writePoblacion(self):
                self.stringPoblacion = ""
                
                for i in range(len(self.matrizPoblacion)):
                        for j in range(len(self.matrizPoblacion[i])):
                                self.stringPoblacion += (str(self.matrizPoblacion[i][j]))
                                        
                        self.stringPoblacion += "\n"
                #print(self.stringPoblacion)
                print("Largo Matriz" + str(len(self.matrizPoblacion)))
                self.salida = open("output.txt", 'w')
                self.salida.write("GT1\n" + str(self.tamPoblacion) + "\n" + self.stringPoblacion)
                self.salida.close()
    
        def getBest(self):
            listaResulFitness = []
            for i in range(len(self.matrizPoblacion)):
                listaResulFitness.append(self.fitness(self.matrizPoblacion[i]))
            #print(listaResulFitness)
            elMejor = self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]
            print("Cantidad de unos del gen: " + str(elMejor.count(1)))  
            print("El mejor es : " + str(self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]))
            return self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]

        def mutar(self, genHijoA, genHijoB):
            probabilidad = randint(1, 100)
            
            if probabilidad <= self.mutacion:

                numeroDePuntosAMutar = randint(1, self.geneSize())
                listaIndicesAMutar = []

                for i in range(0, numeroDePuntosAMutar):
                    posicionRandom = randint(0, self.geneSize() - 1)
                    listaIndicesAMutar.append(posicionRandom)

                for i in range(len(listaIndicesAMutar)):
                    if i != len(listaIndicesAMutar) - 1:
                        if listaIndicesAMutar[i] == listaIndicesAMutar[i+1]:
                            self.mutar(genHijoA, genHijoB)

                for i in range(len(listaIndicesAMutar)):
                    if genHijoA[listaIndicesAMutar[i]] == 0:
                        genHijoA[listaIndicesAMutar[i]] = 1
                    else:
                        genHijoA[listaIndicesAMutar[i]] = 0

                    if genHijoB[listaIndicesAMutar[i]] == 0:
                        genHijoB[listaIndicesAMutar[i]] = 1
                    else:
                        genHijoB[listaIndicesAMutar[i]] = 0
            ##print("lista de indices a mutar: " + str(listaIndicesAMutar))
                        
            listaRetorno = []
            listaRetorno.append(genHijoA)
            listaRetorno.append(genHijoB)
            return listaRetorno       

        def seleccionarGen(self):

            if self.politica == 0: # Simple al azar

                self.GenPadre = self.matrizPoblacion[self.filaRandomPrimerGen]
                self.GenMadre = self.matrizPoblacion[self.filaRandomSegundoGen]

                #Falta verificar que el numero de puntos no sea mayor al tamaÃ±o del gen

                self.listaPuntosFijos = []

                for i in range(self.numCruces):
                    self.indiceRandom = randint(0, self.geneSize() - 1)
                    self.listaPuntosFijos.append(self.indiceRandom)
                    
                for i in range(len(self.listaPuntosFijos)):
                    if i != len(self.listaPuntosFijos) - 1:
                        if self.listaPuntosFijos[i] == self.listaPuntosFijos[i+1]:
                            self.seleccionarGen()
                            
                self.listaPuntosFijos.sort()
                self.listaPuntosFijos.append(self.geneSize())

                self.Hijo_A = []
                self.Hijo_B = []

                estaArriba = True
                contadorIndices = 0

##                print("LISTAPUNTOSFIJOZZZ")
##
##                print(self.listaPuntosFijos)
##                print("Gen Padre!!!: ")
##                print(self.GenPadre)
                for i in range(len(self.listaPuntosFijos)):
                    while contadorIndices != self.listaPuntosFijos[i]:
                        if estaArriba:
                            self.Hijo_A.append(self.GenPadre[contadorIndices])
                            self.Hijo_B.append(self.GenMadre[contadorIndices])
                            estaArriba = False
                        else:
                            self.Hijo_A.append(self.GenMadre[contadorIndices])
                            self.Hijo_B.append(self.GenPadre[contadorIndices])
                            estaArriba = True
                        contadorIndices += 1

                self.listaHijosMutados = self.mutar(self.Hijo_A, self.Hijo_B)


                return self.listaHijosMutados
    
            elif self.politica == 1: # Rueda de la fortuna
                sumaDeFitnesses = 0
                listaDeFitnesses = []

                for i in range(len(self.matrizPoblacion)):
                    sumaDeFitnesses += self.fitness(self.matrizPoblacion[i])
                    listaDeFitnesses.append(self.fitness(self.matrizPoblacion[i]))

                minimoASumar = min(listaDeFitnesses)

                for i in range(len(listaDeFitnesses)):
                    listaDeFitnesses[i] += abs(minimoASumar) + 1

                sumaDeFitnesses = sum(listaDeFitnesses)
                
##                print("Lista de Fitnesses: " + str(listaDeFitnesses))
##                print("Suma de Fitnesses: " + str(sumaDeFitnesses))

                ruedaDeLaFortuna = []

                for i in range(len(listaDeFitnesses)):
                    indiceARepetir = listaDeFitnesses[i]
                    while indiceARepetir != 0:
                        ruedaDeLaFortuna.append(self.matrizPoblacion[i])
                        indiceARepetir -= 1
                
                self.GenMadre = ruedaDeLaFortuna[randint(0, sumaDeFitnesses) - 1]
                self.GenPadre = ruedaDeLaFortuna[randint(0, sumaDeFitnesses) - 1]

##                print("El padre es: " + str(self.GenPadre))
##                print("La madre es: " + str(self.GenMadre))
                
                if self.GenMadre == self.GenPadre:
                    self.seleccionarGen()

                
                self.Hijo_A = []
                self.Hijo_B = []

                self.listaPuntosFijos = []

                for i in range(0, self.numCruces):
                    self.listaPuntosFijos.append(randint(0, self.geneSize() - 1))

                for i in range(len(self.listaPuntosFijos)):
                    if i != len(self.listaPuntosFijos) - 1:
                        if self.listaPuntosFijos[i] == self.listaPuntosFijos[i+1]:
                            self.seleccionarGen()

                self.listaPuntosFijos.sort()
                self.listaPuntosFijos.append(self.geneSize())
                estaArriba = True
                contadorIndices = 0

               # print("Lista de Puntos Fijos: " +str(self.listaPuntosFijos))
                
                for i in range(len(self.listaPuntosFijos)):
                    while contadorIndices != self.listaPuntosFijos[i]:
                        if estaArriba:
                            self.Hijo_A.append(self.GenPadre[contadorIndices])
                            self.Hijo_B.append(self.GenMadre[contadorIndices])
                            estaArriba = False
                        else:
                            self.Hijo_A.append(self.GenMadre[contadorIndices])
                            self.Hijo_B.append(self.GenPadre[contadorIndices])
                            estaArriba = True
                        contadorIndices += 1

                
                self.listaHijosMutados = self.mutar(self.Hijo_A, self.Hijo_B)

                return self.listaHijosMutados
                    

            else: # Torneo
                listaResulFitness = []
                for i in range(len(self.matrizPoblacion)):
                    listaResulFitness.append(self.fitness(self.matrizPoblacion[i]))

                listaPadres = []#Guarda los dos mejores fitness
                listaPadres.append(listaResulFitness.index(max(listaResulFitness)))
##                print("Listassss : \n")
##                print(listaResulFitness)
##                print(max(listaResulFitness))
                listaResulFitness.pop(listaResulFitness.index(max(listaResulFitness)))
                listaPadres.append(listaResulFitness.index(max(listaResulFitness)))
##                print(max(listaResulFitness))
##                print(listaPadres)

                Padre = self.matrizPoblacion[listaPadres[0]]
                Madre = self.matrizPoblacion[listaPadres[1]]

##                print(Padre, Madre)

                self.listaPuntosFijos = []

                for i in range(self.numCruces):
                    self.indiceRandom = randint(0, self.geneSize() - 1)
                    self.listaPuntosFijos.append(self.indiceRandom)
                    
                for i in range(len(self.listaPuntosFijos)):
                    if i != len(self.listaPuntosFijos) - 1:
                        if self.listaPuntosFijos[i] == self.listaPuntosFijos[i+1]:
                            self.seleccionarGen()
                            
                self.listaPuntosFijos.sort()
                self.listaPuntosFijos.append(self.geneSize())

                self.Hijo_A = []
                self.Hijo_B = []

                estaArriba = True
                contadorIndices = 0
                
                for i in range(len(self.listaPuntosFijos)):
                    while contadorIndices != self.listaPuntosFijos[i]:
                        if estaArriba:
                            self.Hijo_A.append(Padre[contadorIndices])
                            self.Hijo_B.append(Madre[contadorIndices])
                            estaArriba = False
                        else:
                            self.Hijo_A.append(Madre[contadorIndices])
                            self.Hijo_B.append(Padre[contadorIndices])
                            estaArriba = True
                        contadorIndices += 1

##                print("Hijos sin mutar: " + str(self.Hijo_A) + str(self.Hijo_B))
                self.listaHijosMutados = self.mutar(self.Hijo_A, self.Hijo_B)

                return self.listaHijosMutados
            
        def getCantidadDeUnosDeUnGen(self, gen):
            res = 0
            for i in range(len(gen)):
                if gen[i] == 1:
                    res += 1

            return res

        def generacion(self):
            self.filaRandomPrimerGen = 0
            self.filaRandomSegundoGen = 0

            while self.filaRandomPrimerGen == self.filaRandomSegundoGen:
                self.filaRandomPrimerGen = randint(0, self.tamPoblacion - 1)
                self.filaRandomSegundoGen = randint(0, self.tamPoblacion- 1)
            
            self.matrizNuevaGeneracion = []

            mitadTamPoblacion = self.tamPoblacion/2
            mitadTamPoblacion = int(mitadTamPoblacion)
            
            for i in range (0, self.cantGeneraciones):
                print("\nNUMERO DE GENERACION: \n" + str(i))
                for j in range(0, mitadTamPoblacion):
                    self.matrizNuevaGeneracion.append(self.seleccionarGen()[0])
                    self.matrizNuevaGeneracion.append(self.seleccionarGen()[1])
                    
                self.matrizPoblacion = copy.deepcopy(self.matrizNuevaGeneracion)
                self.writePoblacion()
                del self.matrizNuevaGeneracion[:]
                self.matrizNuevaGeneracion[:] = []

            #self.matrizPoblacion = copy.deepcopy(self.matrizNuevaGeneracion)
##            print("Matriz Nueva poblacion y largo \n" )
##            print(self.matrizNuevaGeneracion)
##            print(len(self.matrizNuevaGeneracion))
##            print("\nantes de escribir")
            
            #self.writePoblacion()
##            print("despues de escribir")
                    
##            print("GENEIACIONES!!!!!!  "+str(self.matrizNuevaGeneracion))


            existeAlMenosUnGenValido = False

            for i in range(len(self.matrizPoblacion)):
                if self.getCantidadDeUnosDeUnGen(self.matrizPoblacion[i]) <= self.tamanioRecubrimiento:
                    existeAlMenosUnGenValido = True

            if existeAlMenosUnGenValido == True:
                print("Existe al menos un gen válido en la población")
           
            print("El fitness del mejor gen es: " + str(self.fitness(self.getBest())))
            
            

#Falta verificar que la poblaciÃƒÂ³n sea vÃƒÂ¡lida con el tamaÃƒÂ±o de recubrimiento
#Falta hacer la restricciÃƒÂ³n en caso de que el tamaÃƒÂ±o de poblaciÃƒÂ³n sea cero 

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
                     self.universo = []
                     self.subconjuntosBinarios = []
                     self.nuevaPoblacion = []
                     
                     
##    def resetPoblacion(self, tamano):
##        pass
##
        def readProblema(self):
               
                self.archi = open("problemaRec.txt" , 'r')
                
                self.nombre = self.archi.readline()#Nombre del problema

                listaParametros = self.archi.readline().replace("\n", "")
                listaParametros = listaParametros.split()
                
                self.tamUniverso = int(listaParametros[0])
                self.cantSubconjuntos = int(listaParametros[1])
                self.cantSubconjuntosDeseados = int(listaParametros[2])
                
                self.linea = self.archi.readline()
                while self.linea != "":
                    listaSubconjunto = self.linea.replace("\n", "")
                    listaSubconjunto = listaSubconjunto.split()
                    self.subconjuntos.append(listaSubconjunto)
                    self.linea = self.archi.readline()
                self.archi.close()
                
                for i in range(len(self.subconjuntos)):#Ordena la matriz
                    self.subconjuntos[i].sort()
                print("Subconjuntos: " + str(self.subconjuntos))
                
                for i in range(len(self.subconjuntos)):# Crea el universo
                    for j in range(len(self.subconjuntos[i])):
                        if self.subconjuntos[i][j] not in self.universo:
                            self.universo.append(self.subconjuntos[i][j])
                self.universo.sort()
                print("Universo: " + str(self.universo))

                for i in range(len(self.subconjuntos)):#Crea la matriz vacia
                    self.subconjuntosBinarios.append([])
                    
                for i in range(len(self.subconjuntosBinarios)):#Traduce los subconjuntos a 1 y 0
                    for j in range(len(self.universo)):
                        if self.universo[j] not in self.subconjuntos[i]:
                            self.subconjuntosBinarios[i].append(0)
                        else:
                            self.subconjuntosBinarios[i].append(1)
        
                print("Subconjuntos binarios: " +str(self.subconjuntosBinarios))
                    

        def readPoblacion(self):
                self.datos = open("datosRecMin.txt", 'r')
                
                self.matrizPoblacion = [] #Matriz final en donde quedarÃƒÂ¡ guardada la poblaciÃƒÂ³n
                self.listaGen = [] #Lista auxiliar para ciclo
                saltoLinea = 0 #Variable para indicar el comienzo de la poblaciÃƒÂ³n en archivo

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
                print("Poblacion: " + str(self.matrizPoblacion)+ "\n")

        def geneSize(self):
            return self.cantSubconjuntos
            
                
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
            self.gen = gen
            self.resulFitness = 0
            self.listaSubconjuntosGen = []
            self.universoFinal = []
            for i in range(len(gen)):
                if gen[i] == 1:
                    self.listaSubconjuntosGen.append(self.subconjuntos[i])
            
            #print("\ngen"+str(self.gen))
            #print("Lista subconjuntos gen"+str(self.listaSubconjuntosGen)+"\n")
            for i in range(len(self.listaSubconjuntosGen)):
                for j in range (len(self.listaSubconjuntosGen[i])):
                    if self.listaSubconjuntosGen[i][j] not in self.universoFinal:
                        self.universoFinal.append(self.listaSubconjuntosGen[i][j])
            self.universoFinal.sort()                    
            if self.universoFinal == self.universo:
                self.resulFitness = len(self.listaSubconjuntosGen)
                
            else:
                self.resulFitness = len(self.listaSubconjuntosGen) + len(self.subconjuntos)
            #print(self.listaSubconjuntosGen)
            #print("Univeso Final: " + str(self.universoFinal))
            #print("Fitness: " + str(self.resulFitness))
            return self.resulFitness
    
        def getBest(self):
            listaResulFitness = []
            for i in range(len(self.matrizPoblacion)):
                listaResulFitness.append(self.fitness(self.matrizPoblacion[i]))
            #print(listaResulFitness)
            elMejor = self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]
            print("Cantidad de unos del gen: " + str(elMejor.count(1)))  
            print("El mejor es : " + str(self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]))
            return self.matrizPoblacion[listaResulFitness.index(max(listaResulFitness))]
            print("El mejor es : " + str(self.matrizPoblacion[listaResulFitness.index(min(listaResulFitness))]))
            return self.matrizPoblacion[listaResulFitness.index(min(listaResulFitness))]
        
        def mutar(self, genHijoA, genHijoB):
##            print("Indice Mutacion : " + str(self.mutacion))
            probabilidad = 1
            
            if probabilidad <= self.mutacion:

                numeroDePuntosAMutar = randint(1, len(self.matrizPoblacion[0]))
                listaIndicesAMutar = []

                for i in range(0, numeroDePuntosAMutar):
                    posicionRandom = randint(0, len(self.matrizPoblacion[0]) - 1)
                    listaIndicesAMutar.append(posicionRandom)

                for i in range(len(listaIndicesAMutar)):
                    if i != len(listaIndicesAMutar) - 1:
                        if listaIndicesAMutar[i] == listaIndicesAMutar[i+1]:
                            self.mutar(genHijoA, genHijoB)

                for i in range(len(listaIndicesAMutar)):
                    if genHijoA[listaIndicesAMutar[i]] == 0:
                        genHijoA[listaIndicesAMutar[i]] = 1
                    else:
                        genHijoA[listaIndicesAMutar[i]] = 0

                    if genHijoB[listaIndicesAMutar[i]] == 0:
                        genHijoB[listaIndicesAMutar[i]] = 1
                    else:
                        genHijoB[listaIndicesAMutar[i]] = 0
                        
##            print("lista de indices a mutar: " + str(listaIndicesAMutar))
                        
            listaRetorno = []
            listaRetorno.append(genHijoA)
            listaRetorno.append(genHijoB)
            return listaRetorno
        

        def seleccionarGen(self):

            if self.politica == 0: # Simple al azar
                self.filaRandomPrimerGen = randint(0, len(self.matrizPoblacion) - 1)
                self.filaRandomSegundoGen = randint(0, len(self.matrizPoblacion) - 1)

                if self.filaRandomPrimerGen == self.filaRandomSegundoGen:
                       self.seleccionarGen()

                self.GenPadre = self.matrizPoblacion[self.filaRandomPrimerGen]
                self.GenMadre = self.matrizPoblacion[self.filaRandomSegundoGen]

                #Falta verificar que el numero de puntos no sea mayor al tamaÃ±o del gen

                self.listaPuntosFijos = []

                for i in range(self.numCruces):
                    self.indiceRandom = randint(0, len(self.matrizPoblacion[i]) - 1)
                    self.listaPuntosFijos.append(self.indiceRandom)
                    
                for i in range(len(self.listaPuntosFijos)):
                    if i != len(self.listaPuntosFijos) - 1:
                        if self.listaPuntosFijos[i] == self.listaPuntosFijos[i+1]:
                            self.seleccionarGen()
                            
                self.listaPuntosFijos.sort()
                self.listaPuntosFijos.append(self.geneSize())

                self.Hijo_A = []
                self.Hijo_B = []

                estaArriba = True
                contadorIndices = 0
                
                for i in range(len(self.listaPuntosFijos)):
                    while contadorIndices != self.listaPuntosFijos[i]:
                        if estaArriba:
                            self.Hijo_A.append(self.GenPadre[contadorIndices])
                            self.Hijo_B.append(self.GenMadre[contadorIndices])
                            estaArriba = False
                        else:
                            self.Hijo_A.append(self.GenMadre[contadorIndices])
                            self.Hijo_B.append(self.GenPadre[contadorIndices])
                            estaArriba = True
                        contadorIndices += 1

                self.listaHijosMutados = self.mutar(self.Hijo_A, self.Hijo_B)

                eleccionFinal = randint(0, 1)

                return self.listaHijosMutados[eleccionFinal]
    
            elif self.politica == 1: # Rueda de la fortuna
                sumaDeFitnesses = 0
                listaDeFitnesses = []

                for i in range(len(self.matrizPoblacion)):
                    sumaDeFitnesses += self.fitness(self.matrizPoblacion[i])
                    listaDeFitnesses.append(self.fitness(self.matrizPoblacion[i]))

                minimoASumar = min(listaDeFitnesses)

                for i in range(len(listaDeFitnesses)):
                    listaDeFitnesses[i] += abs(minimoASumar) + 1

                sumaDeFitnesses = sum(listaDeFitnesses)
                
##                print("Lista de Fitnesses: " + str(listaDeFitnesses))
##                print("Suma de Fitnesses: " + str(sumaDeFitnesses))

                ruedaDeLaFortuna = []

                for i in range(len(listaDeFitnesses)):
                    indiceARepetir = listaDeFitnesses[i]
                    while indiceARepetir != 0:
                        ruedaDeLaFortuna.append(self.matrizPoblacion[i])
                        indiceARepetir -= 1
                
                self.GenMadre = ruedaDeLaFortuna[randint(0, sumaDeFitnesses) - 1]
                self.GenPadre = ruedaDeLaFortuna[randint(0, sumaDeFitnesses) - 1]

##                print("El padre es: " + str(self.GenPadre))
##                print("La madre es: " + str(self.GenMadre))
                
                if self.GenMadre == self.GenPadre:
                    self.seleccionarGen()

                
                self.Hijo_A = []
                self.Hijo_B = []

                self.listaPuntosFijos = []

                for i in range(0, self.numCruces):
                    self.listaPuntosFijos.append(randint(0, len(self.matrizPoblacion[0]) - 1))

                for i in range(len(self.listaPuntosFijos)):
                    if i != len(self.listaPuntosFijos) - 1:
                        if self.listaPuntosFijos[i] == self.listaPuntosFijos[i+1]:
                            self.seleccionarGen()

                self.listaPuntosFijos.sort()
                self.listaPuntosFijos.append(self.geneSize())
                estaArriba = True
                contadorIndices = 0

                print("Lista de Puntos Fijos: " +str(self.listaPuntosFijos))
                
                for i in range(len(self.listaPuntosFijos)):
                    while contadorIndices != self.listaPuntosFijos[i]:
                        if estaArriba:
                            self.Hijo_A.append(self.GenPadre[contadorIndices])
                            self.Hijo_B.append(self.GenMadre[contadorIndices])
                            estaArriba = False
                        else:
                            self.Hijo_A.append(self.GenMadre[contadorIndices])
                            self.Hijo_B.append(self.GenPadre[contadorIndices])
                            estaArriba = True
                        contadorIndices += 1

                print("Hijo A: "+str(self.Hijo_A))
                print("Hijo B: "+str(self.Hijo_B))
                
                self.listaHijosMutados = self.mutar(self.Hijo_A, self.Hijo_B)

                eleccionFinal = randint(0, 1)

                return self.listaHijosMutados[eleccionFinal]
                        
                

                print(genGanador)

            else: # Torneo
                listaResulFitness = []
                for i in range(len(self.matrizPoblacion)):
                    listaResulFitness.append(self.fitness(self.matrizPoblacion[i]))

                listaPadres = []#Guarda los dos mejores fitness
                listaPadres.append(listaResulFitness.index(max(listaResulFitness)))
##                print("Listassss : \n")
##                print(listaResulFitness)
##                print(max(listaResulFitness))
                listaResulFitness.pop(listaResulFitness.index(max(listaResulFitness)))
                listaPadres.append(listaResulFitness.index(max(listaResulFitness)))
##                print(max(listaResulFitness))
##                print(listaPadres)

                Padre = self.matrizPoblacion[listaPadres[0]]
                Madre = self.matrizPoblacion[listaPadres[1]]

##                print(Padre, Madre)

                self.listaPuntosFijos = []

                for i in range(self.numCruces):
                    self.indiceRandom = randint(0, len(self.matrizPoblacion[i]) - 1)
                    self.listaPuntosFijos.append(self.indiceRandom)
                    
                for i in range(len(self.listaPuntosFijos)):
                    if i != len(self.listaPuntosFijos) - 1:
                        if self.listaPuntosFijos[i] == self.listaPuntosFijos[i+1]:
                            self.seleccionarGen()
                            
                self.listaPuntosFijos.sort()
                self.listaPuntosFijos.append(len(self.matrizPoblacion[i]))

                self.Hijo_A = []
                self.Hijo_B = []

                estaArriba = True
                contadorIndices = 0
                
                for i in range(len(self.listaPuntosFijos)):
                    while contadorIndices != self.listaPuntosFijos[i]:
                        if estaArriba:
                            self.Hijo_A.append(Padre[contadorIndices])
                            self.Hijo_B.append(Madre[contadorIndices])
                            estaArriba = False
                        else:
                            self.Hijo_A.append(Madre[contadorIndices])
                            self.Hijo_B.append(Padre[contadorIndices])
                            estaArriba = True
                        contadorIndices += 1

##                print("Hijos sin mutar: " + str(self.Hijo_A) + str(self.Hijo_B))
                self.listaHijosMutados = self.mutar(self.Hijo_A, self.Hijo_B)

                eleccionFinal = randint(0, 1)
##                print("Numero de Curces: " + str(self.numCruces))
                
##                print("Hijos Mutados: " + str(self.listaHijosMutados))

                return self.listaHijosMutados
            
        def getCantidadDeUnosDeUnGen(self, gen):
            res = 0
            for i in range(len(gen)):
                if gen[i] == 1:
                    res += 1

            return res
            
        def generacion(self):
            self.filaRandomPrimerGen = 0
            self.filaRandomSegundoGen = 0

            while self.filaRandomPrimerGen == self.filaRandomSegundoGen:
                self.filaRandomPrimerGen = randint(0, self.tamPoblacion - 1)
                self.filaRandomSegundoGen = randint(0, self.tamPoblacion- 1)
            
            self.matrizNuevaGeneracion = []

            mitadTamPoblacion = self.tamPoblacion/2
            mitadTamPoblacion = int(mitadTamPoblacion)
            
            for i in range (0, self.cantGeneraciones):
                print("\nNUMERO DE GENERACION: \n" + str(i))
                for j in range(0, mitadTamPoblacion):
                    self.matrizNuevaGeneracion.append(self.seleccionarGen()[0])
                    self.matrizNuevaGeneracion.append(self.seleccionarGen()[1])
                    
                self.matrizPoblacion = copy.deepcopy(self.matrizNuevaGeneracion)
                self.writePoblacion()
                del self.matrizNuevaGeneracion[:]
                self.matrizNuevaGeneracion[:] = []            
             

            existeAlMenosUnGenValido = False

            for i in range(len(self.matrizPoblacion)):
                if self.getCantidadDeUnosDeUnGen(self.matrizPoblacion[i]) <= self.tamanioRecubrimiento:
                    existeAlMenosUnGenValido = True

            if existeAlMenosUnGenValido == True:
                print("Existe al menos un gen válido en la población")
                

    
###############################################-----PROGRAMA-----###############################################


def main():

	stringInstrucciones = "genetico gt1.txt datosVertex.txt 5 5000 1 0 output.txt"
	listaInstrucciones = stringInstrucciones.split()
##	print(listaInstrucciones)

	pCantGeneraciones = int(listaInstrucciones[3])
	pTamPoblacion = int(listaInstrucciones[4])
	pMutacion = int(listaInstrucciones[5])
	pPolitica = int(listaInstrucciones[6])

	numeroDeCruces = 1

	print("\nVERTEX\n" )
	x = Vertex(pPolitica, numeroDeCruces, pMutacion, pTamPoblacion, pCantGeneraciones)
	x.readPoblacion()
	x.readProblema()
	x.generacion()


##	print("\nRECUBRIMIENTO\n" )
##	stringInstrucciones = "genetico problemRec.txt datosRecMin.txt 100 1000 100 2 output.txt"
##	listaInstrucciones = stringInstrucciones.split()
##	print(listaInstrucciones)
##
##	pCantGeneraciones = int(listaInstrucciones[3])
##	pTamPoblacion = int(listaInstrucciones[4])
##	pMutacion = int(listaInstrucciones[5])
##	pPolitica = int(listaInstrucciones[6])
##
##	#
##	numeroDeCruces = 2
##	genRecPrueba = [0,1,0,0,1]
##	r = Recubrimiento(pPolitica, numeroDeCruces, pMutacion, pTamPoblacion,  pCantGeneraciones)
##	r.readPoblacion()
##	r.readProblema()
##
##	r.generacion()
##
##	r.getBest()
##	r.seleccionarGen()

    
if __name__ == "__main__":
    main()
