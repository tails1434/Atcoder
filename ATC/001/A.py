H, W = map(int, input().split())
maps = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maps[i][j] == 's':
            start = (i,j)
        if maps[i][j] == 'g':
            goal = (i,j)

flag = [[False] * W for _ in range(H)]

def dfs(x,y):
    if (not 0 <= x < H) or (not 0 <= y < W):
        return
    if maps[x][y] == '#':
        return
    if flag[x][y]:
        return
    flag[x][y] = True
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

dfs(start[0],start[1])
if flag[goal[0]][goal[1]]:
    print('Yes')
else:
    print('No')