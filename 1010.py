id1, units1, price1 = input().split(' ')
id2, units2, price2 = input().split(' ')
print('VALOR A PAGAR: R$', '{:.2f}'.format(int(units1) * float(price1) + int(units2) * float(price2)))