def warshall_floyd(d,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d

# N:頂点, M:辺
N, M = map(int, input().split())

d = [[float('inf') for i in range(N)] for i in range(N)]

edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
    edges.append([a,b,c])

for i in range(N):
    d[i][i] = 0

warshall_floyd(d,N)
cnt = 0
for edge in edges:
    if d[edge[0]][edge[1]] != edge[2]:
        cnt += 1

print(cnt)