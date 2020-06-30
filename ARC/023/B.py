from collections import deque
import sys
sys.setrecursionlimit(4100000)

def main():
    R, C, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(R)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    Q = deque([[0,0,0]])
    ans = 0
    visited = [[False] * C for _ in range(R)]
    while Q:
        x, y, cnt = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < C and 0 <= ny < R:
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                
                if (cnt+1) % 2 == D % 2:
                    ans = max(ans, A[ny][nx])
                
                if cnt + 1 < D:
                    Q.append([nx,ny,cnt+1])
                    


    print(ans)



if __name__ == "__main__":
    main()