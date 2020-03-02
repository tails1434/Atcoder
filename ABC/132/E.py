from collections import deque
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)

    S, T = map(int, input().split())
    S -= 1
    T -= 1
    dist = [[float('inf')] * 3 for _ in range(N)]
    dist[S][0] = 0
    q = deque([])
    q.append((S,0))
    while q:
        v, l = q.popleft()
        nl = (l + 1) % 3
        for nv in edge[v]:
            if dist[nv][nl] != float('inf'):
                continue
            dist[nv][nl] = dist[v][l] + 1
            q.append((nv,nl))
        
    
    if dist[T][0] == float('inf'):
        print(-1)
    else:
        print(dist[T][0] // 3)




if __name__ == "__main__":
    main()