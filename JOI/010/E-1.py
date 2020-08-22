from collections import deque
import sys
sys.setrecursionlimit(1000000)

def main():
    H, W, N = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == 'S':
                sy = i
                sx = j
                break
    Q = deque([[sx,sy]])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    cnt = 1
    ans = 0
    d = [[float('inf')] * W for _ in range(H)]
    d[sy][sx] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H:
                if C[ny][nx] != 'X' and d[ny][nx] == float('inf'):
                    d[ny][nx] = d[y][x] + 1
                    Q.append([nx,ny])
                    if C[ny][nx] == str(cnt):
                        ans += d[ny][nx]
                        d = [[float('inf')] * W for _ in range(H)]
                        d[ny][nx] = 0
                        if cnt == N:
                            Q = deque([])
                        else:
                            Q = deque([[nx,ny]])
                            cnt += 1
                        break

    print(ans)


if __name__ == "__main__":
    main()