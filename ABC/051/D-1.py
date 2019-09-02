def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d

N, M = map(int, input().split())
d = [[float('inf') for i in range(N)] for i in range(N)]
edges = []

for i in range(M):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
    edges.append([a,b,c])

warshall_floyd(d)

# 与えられた頂点間の辺の距離が求めた最短距離より大きければ
# その辺は使われない
cnt = 0
for edge in edges:
    if d[edge[0]][edge[1]] != edge[2]:
        cnt += 1

print(cnt)