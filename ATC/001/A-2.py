from collections import deque

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    Q = deque([])
    for h in range(H):
        for w in range(W):
            if C[h][w] == 's':
                Q.append([h,w])
                visited[h][w] = True
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while Q:
        y, x = Q.pop()
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < H and 0 <= nx < W:
                if C[ny][nx] == 'g':
                    print('Yes')
                    exit()
                if visited[ny][nx] == False and C[ny][nx] == '.':
                    Q.append([ny,nx])
    print('No')
if __name__ == "__main__":
    main()