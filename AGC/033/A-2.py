from collections import deque
import sys
sys.setrecursionlimit(4100000)
def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    Q = deque([])
    visited = [[float('inf')] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if A[h][w] == '#':
                Q.append((h,w))
                visited[h][w] = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    ans = 0
    while Q:
        y, x = Q.popleft()
        now = visited[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < W and 0 <= ny < H:
                if visited[ny][nx] == float('inf'):
                    visited[ny][nx] = now + 1
                    Q.append((ny,nx))
                    ans = max(ans, now + 1)

    print(ans)




if __name__ == "__main__":
    main()
