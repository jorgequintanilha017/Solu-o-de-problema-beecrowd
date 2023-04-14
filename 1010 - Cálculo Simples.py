peca_1_codigo, peca_1_quantidade, peca_1_valor = input().split()
peca_2_codigo, peca_2_quantidade, peca_2_valor = input().split()
valor = '{:5.2f}'.format(round(int(peca_1_quantidade) * float(peca_1_valor) + int(peca_2_quantidade) * float(peca_2_valor), 2))
print(f"VALOR A PAGAR: R$ {valor}")