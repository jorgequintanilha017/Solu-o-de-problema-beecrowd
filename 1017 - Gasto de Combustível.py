tempo_viagem = int(input())
velocidade_media = int(input())

gasto_medio = 12

distancia_percorrida = tempo_viagem * velocidade_media
litros_necessarios = distancia_percorrida / gasto_medio

print(f"{litros_necessarios:.3f}")