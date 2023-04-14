valor = int(input())
print(valor)

cedulas = (100, 50, 20, 10, 5, 2, 1)

for cedula in cedulas:
    notas_inteiras = valor // cedula
    print(f"{notas_inteiras} nota(s) de R$ {cedula},00")
    valor -= notas_inteiras * cedula