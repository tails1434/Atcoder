import sys
input = sys.stdin.readline

def warshal_floyd(d,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])

    return d

def main():
    N, M, L = map(int, input().split())
    d = [[float('inf')] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        d[A][B] = C
        d[B][A] = C

    e = warshal_floyd(d,N)
    f = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if e[i][j] <= L:
                f[i][j] = 1

    g = warshal_floyd(f,N)
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        if g[s][t] == float('inf'):
            print(-1)
        else:
            print(g[s][t]-1)
    



if __name__ == "__main__":
    main()