import heapq

def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    for i in range(N):
        edge[i].sort()
    
    ans = []
    visited = [False] * N
    Q = [0]
    heapq.heapify(Q)
    while Q:
        q = heapq.heappop(Q)
        ans.append(q+1)
        visited[q] = True
        for v in edge[q]:
            if visited[v]:
                continue
            heapq.heappush(Q, v)

    print(*ans)


if __name__ == "__main__":
    main()