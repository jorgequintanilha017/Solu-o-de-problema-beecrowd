tempo_em_segundos = int(input())

formatos = (3600, 60, 1)
parciais = []

for formato in formatos:
    parcial = tempo_em_segundos // formato
    parciais.append(str(parcial))
    tempo_em_segundos -= parcial * formato
    
print(':'.join(parciais))