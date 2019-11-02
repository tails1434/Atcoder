from collections import deque

def bfs(N, d, ans):
    Q = deque([0])
    visited = [False] * N
    visited[0] = True
    while Q:
        q = Q.popleft()

        for p in d[q]:
            if visited[p]:
                continue
            visited[p] = True
            Q.append(p)
            ans[p] += ans[q]

    return ans


def main():
    N, Q = map(int, input().split())
    d = [[] for _ in range(N)]

    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d[a].append(b)
        d[b].append(a)

    ans = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        ans[p] += x

    print(*bfs(N, d, ans))
    

main()