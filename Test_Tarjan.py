from TAD_Tarjan import *


print("EJEMPLO DE LA PRESENTACIÓN")
print("--------------------------")

grafo_ejemplo = Grafo()

grafo_ejemplo.insertar('A', 'B')
grafo_ejemplo.insertar('B', 'E')
grafo_ejemplo.insertar('B', 'C')
grafo_ejemplo.insertar('B', 'F')
grafo_ejemplo.insertar('E', 'F')
grafo_ejemplo.insertar('E', 'A')
grafo_ejemplo.insertar('F', 'G')
grafo_ejemplo.insertar('G', 'F')
grafo_ejemplo.insertar('G', 'H')
grafo_ejemplo.insertar('H', 'I')
grafo_ejemplo.insertar('I', 'G')
grafo_ejemplo.insertar('I', 'J')
grafo_ejemplo.insertar('C', 'D')
grafo_ejemplo.insertar('C', 'G')
grafo_ejemplo.insertar('D', 'C')
grafo_ejemplo.insertar('D', 'H')


print("Representación del grafo inicial: ")
print("--------------------------")
grafo_ejemplo.imprimir()
print("--------------------------")

print("Aplicamos el algoritmo de Tarjan: ")
print("--------------------------")
grafo_ejemplo.tarjan()

