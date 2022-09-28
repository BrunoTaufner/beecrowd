def entradaDepoisC(c):
    while c >= 0:
        o, d, t = input()
        o = int(o)
        d = int(d)
        t = int(t)

        c -= 1


def leDados(m):
    while m >= 0:
        u, v, w = input().split(' ')
        u = float(u)
        v = float(v)
        w = float(w)

        if (1 <= u and v <= n) and 0 <= w <= 100:
            c = int(input())
            entradaDepoisC(c)

        else:
            break
        m -= 1


n, m = input().split(' ')
n = int(n)
m = int(m)

if 1 <= n <= 100 and 1 <= m <= 10**6:
    leDados(m)
