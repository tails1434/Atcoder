from collections import deque

def main():
    H, W = map(int, input().split())

    field = [list(input()) for i in range(H)]

    cnt = 0
    for i in range(H):
        cnt += field[i].count('.')
    
    def bfs():
        d = [[float('inf')] * W for i in range(H)]

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        que = deque([])
        que.append((0,0))
        d[0][0] = 1

        while que:
            y,x = que.popleft()
            if y == H - 1 and x == W - 1:
                return d[y][x]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < W and 0 <= ny < H and field[ny][nx] != '#' and d[ny][nx] == float('inf'):
                    que.append((ny,nx))
                    d[ny][nx] = d[y][x] + 1

        return -1

    num = bfs()

    if num == -1:
        print(num)
    else:
        print(cnt - num)

main()