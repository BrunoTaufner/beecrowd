
def verifica(cartas: [[]]):
    soma = 0
    pilha = []
    m = 0
    while m < len(cartas):
        n = 0
        while n < len(cartas[m]):
            if cartas[m][n] >= 3:
                cartas[m][n] -= 3
                soma += 1
                if cartas[m][n] >= 3:
                    n -= 1
            elif cartas[m][n] > 0 and (m, n) not in pilha:
                if len(pilha) <= 1:
                    cartas[m][n] -= 1
                    pilha.append((m, n))
                elif len(pilha) == 2:
                    if pilha[0][1] != pilha[1][1] and pilha[0][0] != pilha[1][0] \
                            and pilha[0][0] != m and pilha[1][0] != m and pilha[0][1] != n and pilha[1][1] != n:
                        cartas[m][n] -= 1
                        pilha.append((m, n))
                    elif (pilha[0][1] == pilha[1][1] and pilha[0][0] != pilha[1][0]) or (pilha[0][1] != pilha[1][1] and pilha[0][0] == pilha[1][0]):
                        cartas[m][n] -= 1
                        pilha.append((m, n))
            if len(pilha) == 3:
                pilha.clear()
                soma += 1
                m = 0
            n += 1
        m += 1

    return soma


N = int(input())
while N != 0:
    baralho = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
    i = 0
    while i < N:
        num, forma = input().split(' ')

        if num == 'um':
            if 'quadrado' in forma:
                baralho[0][0] += 1
            elif 'triangulo' in forma:
                baralho[0][1] += 1
            else:
                baralho[0][2] += 1
        elif num == 'dois':
            if 'quadrado' in forma:
                baralho[1][0] += 1
            elif 'triangulo' in forma:
                baralho[1][1] += 1
            else:
                baralho[1][2] += 1
        else:
            if 'quadrado' in forma:
                baralho[2][0] += 1
            elif 'triangulo' in forma:
                baralho[2][1] += 1
            else:
                baralho[2][2] += 1
        i += 1

    print(verifica(baralho))
    N = int(input())
