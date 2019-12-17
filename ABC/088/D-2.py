from collections import deque

def main():
    H, W = map(int, input().split())
    S = list(input() for _ in range(H))

    Q = deque([(0, 0)])
    d = [[float('inf')] * W for _ in range(H)]
    d[0][0] = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while Q:
        h, w = Q.popleft()

        if h == H - 1 and w == W - 1:
            break

        for i in range(4):
            nh = h + dy[i]
            nw = w + dx[i]

            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and d[nh][nw] == float('inf'):
                d[nh][nw] = min(d[nh][nw], d[h][w] + 1)
                Q.append((nh,nw))

    if d[H-1][W-1] == float('inf'):
        print(-1)
        exit()
    cnt = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                cnt += 1

    print(cnt - d[H-1][W-1] - 1)

         

    


if __name__ == "__main__":
    main()