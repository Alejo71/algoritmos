import sys

class Nodo:
    def __init__(self, value):
        self.value = value
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.root = None

    def insercion(self, value):
        if self.root is None:
            self.root = Nodo(value)
        else:
            self.insercion_recursiva(self.root, value)

    def insercion_recursiva(self, nodo_actual, value):
        if value < nodo_actual.value:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(value)
            else:
                self.insercion_recursiva(nodo_actual.izquierdo, value)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(value)
            else:
                self.insercion_recursiva(nodo_actual.derecho, value)

    def imprimir_arbol(self, nodo_actual):
       
        if nodo_actual is None:
            return ""
        
        izq = self.imprimir_arbol(nodo_actual.izquierdo)
        der = self.imprimir_arbol(nodo_actual.derecho)
        
        return f"{{{nodo_actual.value}{izq}{der}}}"


def main():
    entrada = sys.stdin.read().strip()
    if not entrada:
        return
    
    elementos = list(map(int, entrada.split()))
    
    arbol = BST()
    for x in elementos:
        arbol.insercion(x)
        
    print(arbol.imprimir_arbol(arbol.root))

if __name__ == "__main__":
    main()