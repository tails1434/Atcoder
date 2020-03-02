import sys
input = sys.stdin.readline

def main():
    N, M, L = map(int, input().split())
    dist = [[float('inf')] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        if C > L:
            continue
        A -= 1
        B -= 1
        dist[A][B] = C
        dist[B][A] = C

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    e = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dist[i][j] <= L:
                e[i][j] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                e[i][j] = min(e[i][j], e[i][k] + e[k][j])


    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        if e[s][t] == float('inf'):
            print(-1)
            continue
        ans = e[s][t]
        print(ans-1)


if __name__ == "__main__":
    main()