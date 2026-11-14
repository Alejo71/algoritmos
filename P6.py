import sys


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def min_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l <= heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest, heap_size)


def extract_min_heap(A, heap_size):
    if heap_size < 1:
        return None, heap_size
    minimo = A[1]
    if heap_size == 1:
        return minimo, 0
    A[1] = A[heap_size]
    heap_size -= 1
    min_heapify(A, 1, heap_size)
    return minimo, heap_size


def insert_min_heap(A, valor, heap_size):
    heap_size += 1
    if heap_size < len(A):
        A[heap_size] = valor
    else:
        A.append(valor)
    i = heap_size
    while i > 1 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
    return heap_size


A = [None]
heap_size = 0
for linea in sys.stdin:
    partes = linea.split()
    if not partes:
        continue
    if partes[0] == "fin":
        break
    if partes[0] == "insertar":
        heap_size = insert_min_heap(A, int(partes[1]), heap_size)
    elif partes[0] == "extraer":
        _, heap_size = extract_min_heap(A, heap_size)
    if heap_size == 0:
        print("Empty")
    else:
        print(" ".join(map(str, A[1:heap_size + 1])))