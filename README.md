# Algoritmo-Tarjan-Python
#Introducción

En el presente repositorio se presentará el algoritmo de Tarjan (1970) el cual fue el primer algoritmo que trabaja en tiempo lineal para encontrar componentes fuertemente conectados o conexos en un grafo dirigido usando una búsqueda en profundidad (DFS).
 Un grafo dirigido está fuertemente conectado si hay un camino entre todos los pares de vértices del grafo, es decir existe un camino por ejemplo desde el primer vértice del par hasta el segundo, y otro camino desde el segundo vértice hasta el primero.
 Por otra parte, mencionaremos que un componente fuertemente conectado de un grafo dirigido es un subgrafo fuertemente conexo de ese grafo. Estos subgrafos forman una partición del grafo. El algortimo de Tarjan no considera la ponderación de las aristas.

 #Procedimiento
![image](https://github.com/user-attachments/assets/b89a595c-c89c-46f2-984a-e8baf4af9eb6)

1- El algoritmo comienza haciendo una búsqueda en profundidad (DFS) que inicia desde un nodo arbitrario a sus nodos adyacentes.

1a-Marcamos ese nodo inicial (y cada nodo no visitado a medida que lo recorremos) con      un valor de visitado (valor numérico), un valor de enlace y lo agregamos a la pila.

 1b-Cada nodo tendrá un valor de visitado (con el que sabremos si fue visitado o no) y un      valor de enlace (valor que tendrá en común dentro del componente fuertemente conectado) que serán seteados en consecuencia al número del nodo que se haya visitado, por ejemplo, en el nodo inicial   su valor de   enlace y valor de visitado será 1.1, el segundo nodo visitado tendrá valor de enlace y valor de visitado de 2.2, y así sucesivamente.
 
 1c- Exploramos los nodos adyacentes al nodo inicial, seteamos sus valores (visitado y enlace) y agregamos a la pila, siguiendo la búsqueda DFS en profundidad.





 




