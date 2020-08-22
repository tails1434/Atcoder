from collections import deque

def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sx -= 1
    sy -= 1
    gx -= 1
    gy -= 1
    D = [list(input()) for _ in range(R)]
    Q = deque([[sx,sy]])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[float('inf')] * C for _ in range(R)]
    visited[sy][sx] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < C and 0 <= ny < C:
                if D[ny][nx] == "." and visited[ny][nx] == float('inf'):
                    visited[ny][nx] = visited[y][x] + 1
                    Q.append([nx,ny])
    print(visited[gy][gx])
    
if __name__ == "__main__":
    main()