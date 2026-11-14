b, r, n = map(int, input().split())
numeros = list(map(int, input().split()))

for posicion in range(0, b, r):

    cantidad_bits = min(r, b - posicion)
    limite = 2 ** cantidad_bits
    mascara = limite - 1
    conteo = [0] * limite

    for numero in numeros:
        digito = (numero >> posicion) & mascara
        conteo[digito] += 1

    for i in range(1, limite):
        conteo[i] += conteo[i - 1]

    ordenados = [0] * n

    for numero in reversed(numeros):
        digito = (numero >> posicion) & mascara
        conteo[digito] -= 1
        ordenados[conteo[digito]] = numero

    numeros = ordenados

    print(*numeros)