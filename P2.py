n = int(input())
for m in range(n):
    k = int(input())
    arreglo_original = [int(a) for a in input().split()]

    # Insertion sort clásico
    arreglo = arreglo_original.copy()
    comparision_classic = 0
    movimiento_classic = 0
    for j in range(1, len(arreglo)):
        key = arreglo[j]
        low = 0
        high = j - 1
        while low <= high:
            comparision_classic += 1
            if arreglo[high] > key:
                arreglo[high + 1] = arreglo[high]
                movimiento_classic += 1
                high -= 1
            else:
                break
        arreglo[high + 1] = key
        movimiento_classic += 1
    # Binary insertion sort
    arreglo = arreglo_original.copy()
    comparision_binary = 0
    movimiento_binary = 0
    for j in range(1, len(arreglo)):
        key = arreglo[j]
        low = 0
        high = j - 1
        while low <= high:
            mid = (low + high) // 2
            comparision_binary += 1
            if arreglo[mid] <= key:
                low = mid + 1
            else:
                high = mid - 1
        for e in range(j - 1, low - 1, -1):
            arreglo[e + 1] = arreglo[e]
            movimiento_binary += 1
        arreglo[low] = key
        movimiento_binary += 1
    print(comparision_classic, movimiento_classic, comparision_binary, movimiento_binary)