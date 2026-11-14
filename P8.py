class Nodo:
    def __init__(self, value):
        self.value = value
        self.izquierdo = None
        self.derecho = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = Nodo("HEAD")
        self.tail = Nodo("TAIL")
        self.head.derecho = self.tail
        self.tail.izquierdo = self.head

    def push_front(self, value):
        nuevo = Nodo(value)
        primer_nodo = self.head.derecho
        nuevo.izquierdo = self.head
        nuevo.derecho = primer_nodo
        self.head.derecho = nuevo
        primer_nodo.izquierdo = nuevo

    def push_back(self, value):
        nuevo = Nodo(value)
        ultimo_nodo = self.tail.izquierdo
        nuevo.derecho = self.tail
        nuevo.izquierdo = ultimo_nodo
        self.tail.izquierdo = nuevo
        ultimo_nodo.derecho = nuevo

    def pop_front(self):
        if self.head.derecho != self.tail:
            nodo = self.head.derecho
            self.head.derecho = nodo.derecho
            nodo.derecho.izquierdo = self.head

    def pop_back(self):
        if self.head.derecho != self.tail:
            nodo = self.tail.izquierdo
            self.tail.izquierdo = nodo.izquierdo
            nodo.izquierdo.derecho = self.tail

    def print_lista(self):
        elementos = ["HEAD"]
        actual = self.head.derecho
        while actual != self.tail:
            elementos.append(str(actual.value))
            actual = actual.derecho
        elementos.append("TAIL")
        print(" <-> ".join(elementos))



n = int(input())
lista = ListaDoblementeEnlazada()

for i in range(n):
    descripcion = input().split()
    op = descripcion[0]

    if op == "P":
        lista.print_lista()
    elif op == "PB":
        lista.push_back(descripcion[1])
    elif op == "PF":
        lista.push_front(descripcion[1])
    elif op == "OB":
        lista.pop_back()
    elif op == "OF":
        lista.pop_front()