total = float(input().replace(',', '.'))
cents = total * 100
n100 = int(total / 100)
aux = total % 100
n50 = int(aux / 50)
aux = aux % 50
n20 = int(aux / 20)
aux = aux % 20
n10 = int(aux / 10)
aux = aux % 10
n5 = int(aux / 5)
aux = aux % 5
n2 = int(aux / 2)
aux = aux % 2
n1 = int(aux)
cents %= 100
c50 = int(cents / 50)
cents %= 50
c25 = int(cents / 25)
cents %= 25
c10 = int(cents / 10)
cents %= 10
c5 = int(cents / 5)
cents %= 5
c1 = int(cents)
print("NOTAS:")
print(n100, 'nota(s) de R$ 100.00')
print(n50, 'nota(s) de R$ 50.00')
print(n20, 'nota(s) de R$ 20.00')
print(n10, 'nota(s) de R$ 10.00')
print(n5, 'nota(s) de R$ 5.00')
print(n2, 'nota(s) de R$ 2.00')
print("MOEDAS:")
print(n1, 'moeda(s) de R$ 1.00')
print(c50, 'moeda(s) de R$ 0.50')
print(c25, 'moeda(s) de R$ 0.25')
print(c10, 'moeda(s) de R$ 0.10')
print(c5, 'moeda(s) de R$ 0.05')
print(c1, 'moeda(s) de R$ 0.01')
