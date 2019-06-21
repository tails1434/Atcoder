map = [input() for _ in range(10)]

# 陸地をカウントする
cnt = 0
for i in range(10):
    cnt += map[i].count('o')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    global number
    seen[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (not 0 <= nx < 10) or (not 0 <= ny <10):
            continue
        
        if map[nx][ny] == 'x':
            continue
        
        if seen[nx][ny]:
            continue
        
        number += 1
        dfs(nx,ny)

for i in range(10):
    for j in range(10):
        number = 0
        seen = [[False] * 10 for i in range(10)]
        if map[i][j] == 'x':
            dfs(i,j)
            if number == cnt:
                print('YES')
                exit()

print('NO')