N, M = map(int, input().split())
graph = [[0 for i in range(N)] for j in range(N)]
edges = []
for m in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append([a,b])
    graph[a][b] = 1
    graph[b][a] = 1

ans = 0
for a,b in edges:
    graph[a][b] = 0
    graph[b][a] = 0

    visited = [False] * N
    visited[0] = True
    q = [i for i in range(N) if graph[0][i]]

    while q:
        r = q.pop(0)
        visited[r] = True
        for i in range(N):
            if graph[r][i] and not visited[i]:
                q.append(i)

    if False in visited:
        ans += 1

    graph[a][b] = 1
    graph[b][a] = 1

print(ans)