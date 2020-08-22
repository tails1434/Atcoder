from collections import deque

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    d = [[float('inf')] * W for _ in range(H)]
    Q = deque([])
    for h in range(H):
        for w in range(W):
            if A[h][w] == '#':
                d[h][w] = 0
                Q.append([h,w])
    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    while Q:
        h,w = Q.popleft()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < H and 0 <= nw < W:
                if A[nh][nw] == '.' and d[nh][nw] == float('inf'):
                    A[nh][nw] = '#'
                    d[nh][nw] = min(d[nh][nw], d[h][w] + 1)
                    Q.append([nh,nw])

    ans = 0
    for h in range(H):
        ans = max(ans, max(d[h]))

    print(ans)
    


if __name__ == "__main__":
    main()