def fuerza_bruta(a):
    inv = 0
    comps = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            comps += 1
            if a[i] > a[j]:
                inv += 1
    return inv, comps


def dividir_conquistar(a):
    
    if len(a) <= 1:
        return a, 0, 0

    mitad = (len(a) + 1) // 2       
    izq, inv_i, comp_i = dividir_conquistar(a[:mitad])
    der, inv_d, comp_d = dividir_conquistar(a[mitad:])

    inv = inv_i + inv_d
    comps = comp_i + comp_d
    mezcla = []
    i = j = 0
    while i < len(izq) and j < len(der):
        comps += 1
        if izq[i] <= der[j]:
            mezcla.append(izq[i])
            i += 1
        else:
            mezcla.append(der[j])
            j += 1
            inv += len(izq) - i
    mezcla += izq[i:] + der[j:]      
    return mezcla, inv, comps


t = int(input())
for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    j, comps_fb = fuerza_bruta(a)
    j, inv, comps_dividir_conquistar = dividir_conquistar(a)
    print(inv, comps_fb, comps_dividir_conquistar)