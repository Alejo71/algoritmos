import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    p = int(input_data[1])
    n = int(input_data[2])
    keys = input_data[3:3 + n]
    
    a = 2654435769
    mask32 = 0xFFFFFFFF
    
    salida = []
    for key_str in keys:
        k = int(key_str)
        r0 = (a * k) & mask32
        h = r0 >> (32 - p)
        bits = f"{h:0{p}b}"
        salida.append(f"{k} {r0} {bits} {h}")
    
    print("\n".join(salida))

if __name__ == "__main__":
    main()