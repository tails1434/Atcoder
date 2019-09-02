import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N)]
    
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)
    
    ans = [0] * N
    for i in range(Q):
        p, x = map(int, input().split())
        p -= 1
        ans[p] += x

    visited = [False] * N
    visited[0] = True
    Q = deque([0])

    while Q:
        p = Q.popleft()

        for q in tree[p]:
            if visited[q]:
                continue
            visited[q] = True
            ans[q] += ans[p]
            Q.append(q)

    print(*ans)
main()