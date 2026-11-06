n = int(input())
for i in range(n):
    lista = [int(a) for a in input().split()]
    a = max(lista)
    b = min(lista) - 1

    sumatoria = a*(a+1)//2 - b*(b+1)//2
    cuadrados = a*(a+1)*(2*a+1)//6 - b*(b+1)*(2*b+1)//6
    cubos = (a*(a+1)//2)**2 - (b*(b+1)//2)**2

    print(sumatoria, cuadrados, cubos)
