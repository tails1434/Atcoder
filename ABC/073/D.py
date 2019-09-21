import itertools

def war(N,d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d

def main():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    d = [[float('inf')] * N for _ in range(N)]

    for i in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        d[A][B] = C
        d[B][A] = C

    for i in range(N):
        d[i][i] = 0

    war(N,d)
    ans = float('inf')

    for a in itertools.permutations(r):
        tmp = 0
        for i in range(len(a)-1):
            tmp += d[a[i]-1][a[i+1]-1]
        ans = min(ans, tmp)

    print(ans)


main()