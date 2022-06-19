class Carta:
    def __init__(self, num, forma):
        self.num = num
        self.forma = forma

def verificaCartas(cartas):

    return 0


N = int(input())
while N != 0:
    baralho = []
    i = 0
    while i < N:
        num, forma = input().split(' ')
        if num == 'um':
            num = 1
        elif num == 'dois':
            num = 2
        else:
            num = 3
        baralho.append(Carta(int(num), forma[:1]))

        i += 1
    N = int(input())
