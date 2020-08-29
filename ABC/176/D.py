from collections import deque
import sys
sys.setrecursionlimit(10**8)

def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    Ch -= 1
    Cw -= 1
    Dh -= 1
    Dw -= 1
    S = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    cnt = [[float('inf')] * W for _ in range(H)]
    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    visited[Ch][Cw] = True
    cnt[Ch][Cw] = 0
    Q = deque([[Ch,Cw]])
    while Q:
        h, w = Q.popleft()
        c = cnt[h][w]
        if h == Dh and w == Dw:
            break
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                if cnt[nh][nw] > c:
                    cnt[nh][nw] = c
                    Q.appendleft([nh,nw])
        nc = c + 1
        for j in range(-2,3):
            for k in range(-2,3):
                nh = h + j
                nw = w + k
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                    if cnt[nh][nw] > nc:
                        cnt[nh][nw] = nc
                        Q.append([nh,nw])

    if cnt[Dh][Dw] == float('inf'):
        print(-1)
    else:
        print(cnt[Dh][Dw])




if __name__ == "__main__":
    main()
