A, B, C = input().split(' ')
greatest = 0
for num in A, B, C:
    if int(num) > greatest:
        greatest = int(num)
print(greatest, 'eh o maior')