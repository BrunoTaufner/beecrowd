def verifica(cartas: [[]]):
    soma = 0
    pilha = []
    numero = 0
    while numero < len(cartas):
        formato = 0
        while formato < len(cartas[numero]):
            if cartas[numero][formato] > 0 and (numero, formato) not in pilha:
                if len(pilha) <= 1:
                    cartas[numero][formato] -= 1
                    pilha.append((numero, formato))
                elif len(pilha) == 2:
                    if (pilha[0][0] != numero and pilha[1][0] != numero
                        and pilha[0][1] != formato and pilha[1][1] != formato) \
                            or (pilha[0][0] != numero and pilha[1][0] != numero
                                and pilha[0][1] == formato and pilha[1][1] == formato) \
                            or (pilha[0][0] == numero and pilha[1][0] == numero
                                and pilha[0][1] == formato and pilha[1][1] == formato):
                        cartas[numero][formato] -= 1
                        pilha.append((numero, formato))
                        numero -= 1
            if len(pilha) == 3:
                pilha.clear()
                soma += 1
                numero = 0
            formato += 1
        numero += 1

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
