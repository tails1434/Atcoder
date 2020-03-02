import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
        
    ans = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1 
        ans[p] += x
    visited = [False] * N
    Q = deque()
    Q.append(0)
    while Q:
        v = Q.popleft()
        visited[v] = True
        for d in edge[v]:
            if visited[d]:
                continue
            Q.append(d)
            ans[d] += ans[v]

    print(*ans)



if __name__ == "__main__":
    main()