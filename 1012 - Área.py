a, b, c = map(float, input().split())
area_triangulo_retangulo = a*c/2
area_circulo = 3.14159*c**2
area_trapezio = (a+b)/2*c
area_quadrado = b**2
area_retangulo = a*b
print(f"TRIANGULO: {area_triangulo_retangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")

#{area:.2f}