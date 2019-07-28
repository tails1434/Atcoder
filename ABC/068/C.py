def main():
    N, M = map(int, input().split())

    # 場所1からいける場所
    s = []

    # 場所Nへいける場所
    g = []

    for i in range(M):
        a,b = map(int, input().split())
        if a == 1:
            s.append(b)
        if b == 1:
            s.append(a)
        if a == N:
            g.append(b)
        if b == N:
            g.append(a)

    s = set(s)
    g = set(g)

    for i in s:
        if i in g:
            print('POSSIBLE')
            exit()
    print('IMPOSSIBLE')

main()