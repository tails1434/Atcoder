from collections import deque

def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
    C = list(map(int, input().split()))
    cnt = [0] * N
    visited = [False] * N
    Q = deque([0])
    while Q:
        q = Q.popleft()
        visited[q] = True
        for v in edge[q]:
            if q == v:
                continue
            if visited[v]:
                continue
            cnt[q] += 1
            Q.append(v)

    tmp = []
    for i in range(N):
        tmp.append((cnt[i],i))
    tmp.sort()
    C.sort()
    d = [0] * N
    for i in range(N):
        d[tmp[i][1]] = C[i]

    print(sum(C) - max(C))
    print(*d)
    


if __name__ == "__main__":
    main()