from collections import deque

H, W = map(int, input().split())
A = [] * H
a = []
for i in range(H):
    A[i] = input()
    for j in range(W):
        if A[i][j] == '#':
            a.append([i,j])

for i in a:
    x,y = i
    print(x,y)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[float('inf')] * W for i in range(H)]

def bfs():
    queue = deque()
    for i in range(H):
      for j in range(W):
        if A[i][j] == '#':
            queue.append([i,j])
            visited[i][j] = 0

    while queue:
        y,x = queue.popleft()
    
        for i in range(4):
            nx = x + dy[i]
            ny = y + dx[i]
    
            if 0 <= ny < H and 0 <= nx < W and visited[ny][nx] == float('inf'):
                queue.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1
    
    tmp = 0
    for k in range(H):
        if tmp < max(visited[k]):
            tmp = max(visited[k])
    
    return tmp

#print(bfs())
            
