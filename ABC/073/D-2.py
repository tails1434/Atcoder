from itertools import permutations

def main():
    N: int
    M: int
    R: int
    A: int
    B: int
    C: int
    ans: int    
    INF: int
    INF = 10 ** 10
    N, M, R = map(int, input().split())
    r: list = list(map(lambda x: x - 1, map(int, input().split())))
    dist :list = [[float('inf')] * N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        dist[A][B] = C
        dist[B][A] = C
    for i in range(N):
        dist[i][i] = 0
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = INF
    for item in permutations(r):
        L: int = len(item)
        d: int = 0
        for i in range(1,L):
            pre: int = item[i-1]
            now: int = item[i]
            d += dist[pre][now]
        ans = min(ans, d)
    print(ans)  

if __name__ == "__main__":
    main()