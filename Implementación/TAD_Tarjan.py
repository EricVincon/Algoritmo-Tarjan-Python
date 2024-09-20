class Arista:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)

    def valor(self):
        return self.dato

    def proximo(self):
        return self.prox

    def imprimeLista(self):
        nodo = self
        while nodo:
            print(nodo, end=" ")
            nodo = nodo.prox
        print(" ")

class Grafo:
    def __init__(self):
        self.lista_vertices = {}
        self.n_arcos = 0

    def __str__(self):
        return f"G = ({self.n_vertices()} V, {self.n_arcos} A)"

    def n_vertices(self):
        return len(self.lista_vertices)

    def vertices(self):
        return self.lista_vertices

    def numero_arcos(self):
        return self.n_arcos
    
    def insertar(self, x, z):
        if x not in self.lista_vertices:
            self.lista_vertices[x] = []  
        if z not in self.lista_vertices:
            self.lista_vertices[z] = []

        self.lista_vertices[x].append(z)  
        self.n_arcos += 1

    
    def primer_adyacente(self, x):
        if x not in self.lista_vertices:
            raise ValueError("El vértice no existe en el diccionario del Grafo")
        else:
            return self.lista_vertices[x]
        
    
    def imprimir(self):
        for vertice in self.lista_vertices:
            print(vertice, end=' ')  # imprimirá cada vértice del grafo diccionario
            arco = self.lista_vertices[vertice]  # asigna a arco la lista de adyacencia del vértice actual
            if arco:  # comprueba si el vértice tiene adyacentes
                print("->", end=' ')
                for adyacente in arco:
                    print(adyacente, end=' ')
                print("")  # Nueva línea después de imprimir todos los adyacentes
            else:
                 print("")

        
        

    def tarjan(self):
        
        """tenemos una funcion interna para realizar la busquedad en profundidad, mi funcion dfs solo se accedera dentro tarjan"""
        
        def dfs(u, visitado, pila, valor_visitado, valor_enlace, id_actual): #variables locales de tarjan
            visitado[u] = True # marca el nodo 'u' como visitado
            valor_visitado[u] = valor_enlace[u] = id_actual
            id_actual += 1
            #tanto el valor_visitado, como valor_enlace se inicializan segun el numero del nodo descubierto y se agrega el nodo a la pila 
            pila.append(u)
            
            """exploracion en profundidad"""
            for v in self.lista_vertices.get(u, []): #itera sobre los nodos adyacentes 'v' del nodo 'u'
                if not visitado.get(v, False):
                    dfs(v, visitado, pila, valor_visitado, valor_enlace, id_actual) #si el nodo'v' no fue visitado, explora sus adyacentes
                    
                if v in pila: # se descubre un nodo 'v' adyacente a 'u' que ya fue visitado y esta en la pila
                    valor_enlace[u] = min(valor_enlace[u], valor_enlace[v]) #actualizamos el valor de enalce de los dos nodos, con el minimo en común

            if valor_visitado[u] == valor_enlace[u]: #encontramos la raiz del componente
                componente_fuertemente_conectada = []
                w = None
                while w != u: #desapilamos los nodos de la pila hasta encontrar de nuevo a 'u'
                    w = pila.pop()
                    componente_fuertemente_conectada.append(w)
                print("Componente fuertemente conectada:", componente_fuertemente_conectada)

        #estructuras para mantener el estado de los nodos durante el proceso
        visitado = {} #clave TRUE -> nodo visitado 
        pila = []
        valor_visitado = {}#indices
        valor_enlace = {}#indices , para asignar valores a los nodos visitados
        id_actual = 0 #contador para asignar los indices a los nodos

        """iteracion inicial. Se llama a dfs. Se asegura que todos los nodos del grafo se visiten(incluso si no estan conectados a otros nodos)"""
        for u in self.lista_vertices:
            if not visitado.get(u, False):
                dfs(u, visitado, pila, valor_visitado, valor_enlace, id_actual)