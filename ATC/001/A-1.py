import sys
sys.setrecursionlimit(10**9)

H, W = map(int, input().split())
field = [input() for i in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 探索したらTrueにする
seen = [[False] * W for i in range(H)]


def dfs(x,y):
    seen[x][y] = True
    
    for i in range(4):
        dh = x + dx[i]
        dw = y + dy[i]

        if (not 0 <= dh < H) or (not 0 <= dw < W):
            continue
        
        if field[dh][dw] == '#':
            continue
        
        if seen[dh][dw]:
            continue

        # if文をすべてパスしたら再帰的に調べる
        dfs(dh,dw)

# fieldからstartとgoalの座標を調べて、startの座標でdfsを実行する
# goalでのseenがtrueだったらYes、FalseだったらNo

for i in range(H):
    for j in range(W):
        if field[i][j] == 's':
            sh = i
            sw = j
        if field[i][j] == 'g':
            gh = i
            gw = j

dfs(sh,sw)

if seen[gh][gw]:
    print('Yes')
else:
    print('No')