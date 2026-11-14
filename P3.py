import math

def mezclar(A, inicio, medio, fin):
    n_izq = medio - inicio + 1
    n_der = fin - medio

    izq = [0] * n_izq
    der = [0] * n_der

    for i in range(n_izq):
        izq[i] = A[inicio + i]

    for j in range(n_der):
        der[j] = A[medio + 1 + j]

    i = 0
    j = 0
    k = inicio

    while i < n_izq and j < n_der:
        if izq[i] <= der[j]:
            A[k] = izq[i]
            i += 1
        else:
            A[k] = der[j]
            j += 1
        k += 1

    while i < n_izq:
        A[k] = izq[i]
        i += 1
        k += 1

    while j < n_der:
        A[k] = der[j]
        j += 1
        k += 1

    print(*A[inicio:fin + 1])
    return A


def ordenar(A, inicio, fin):
    if inicio < fin:
        tercio = math.floor((fin - inicio + 1) / 3)

        if tercio == 0:
            medio = inicio
        else:
            medio = inicio + tercio - 1

        print(*A[inicio:medio + 1])
        ordenar(A, inicio, medio)

        print(*A[medio + 1:fin + 1])
        ordenar(A, medio + 1, fin)

        mezclar(A, inicio, medio, fin)


def main():
    A = list(map(int, input().split()))
    ordenar(A, 0, len(A) - 1)


main()