def menor_subconjunto_nao_gerado(arr):
    arr.sort()
    atual = 0
    for i in range(len(arr)):
        if arr[i] <= atual + 1:
            atual += arr[i]
        else:
            return atual + 1
    return atual + 1


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(menor_subconjunto_nao_gerado(arr))