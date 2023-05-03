def converter(numero):
    if numero.startswith('0x'):
        return int(numero, 16)
    else:
        return '0x' + hex(int(numero))[2:]

while True:
    entrada = input()
    if entrada == '-1':
        break
    saida = converter(entrada)
    print(saida)
