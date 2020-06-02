import sys
from collections import deque
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    edge = [[] * N for _ in range(N)]
    new_edge = [[] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        
    S, T = map(int, input().split())
    S -= 1
    T -= 1
    d = [[float('inf')] * 3 for _ in range(N)]
    q = deque([])
    q.append((S,0))
    d[S][0] = 0
    while q:
        v,l = q.popleft()
        nl = (l + 1) % 3
        for nv in edge[v]:
            if d[nv][nl] != float('inf'):
                continue
            q.append((nv,nl))
            d[nv][nl] = d[v][l] + 1
    if d[T][0] == float('inf'):
        print(-1)
    else:
        print(d[T][0] // 3)
            



if __name__ == "__main__":
    main()
