from collections import deque

H,W = map(int, input().split())
s = [input() for _ in range(H)]

cnt = 0
for i in range(H):
    cnt += s[i].count('.')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[float('inf')] * W for i in range(H)]

def bfs():
    queue = deque([[0,0]])
    visited[0][0] = 1

    while queue:
        y,x = queue.popleft()

        if y == H - 1 and x == W - 1:
            return visited[y][x]
        
        for i in range(4):
            nx = x + dy[i]
            ny = y + dx[i]

            if 0 <= nx < W and 0 <= ny < H and s[ny][nx] != '#' and visited[ny][nx] == float('inf'):
                queue.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1
    
    return -1

num = bfs()

if num == -1:
    print(num)
else:
    print(cnt - num)