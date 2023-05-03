while True:
    n = int(input())
    if n == 0:
        break
        
    palavras = [input() for _ in range(n)]
    palavras.sort()

    conjunto_bom = True
    for i in range(n - 1):
        if palavras[i] == palavras[i + 1][:len(palavras[i])]:
            conjunto_bom = False
            break
    
    if conjunto_bom:
        print("Conjunto Bom")
    else:
        print("Conjunto Ruim")