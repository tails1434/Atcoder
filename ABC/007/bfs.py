from collections import deque

R, C = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())

c = [input() for i in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1



def bfs(sy,sx,gy,gx,c):
    dx = [1, 0 , -1, 0]
    dy = [0, 1, 0, -1]
    # すべての点をINFで初期化
    visited = [[float('inf')]*C for j in range(R)]
    # スタート地点をqueueに入れ、その点の距離を0にする
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0

    # queueが空になるまでループ
    while queue:
        y, x = queue.popleft()
        # 取り出してきた状態がゴールなら探索をやめる
        if y == gy and x == gx:
            return visited[y][x]
        # 移動を四方向ループ
        for i in range(4):
            ny = y + dx[i]
            nx = x + dy[i]

            # 移動可能化の判定とすでに訪れているかを判定(!= INFなら訪れたことがある)
            if 0 <= nx < C and 0 <= ny < R and c[ny][nx] != '#' and visited[ny][nx] == float('inf'):
                # 移動できるならqueueに入れて、距離を+1する
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

print(bfs(sy,sx,gy,gx,c))