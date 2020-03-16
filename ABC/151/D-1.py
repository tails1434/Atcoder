from collections import deque

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    dh = [0,1,0,-1]
    dw = [1,0,-1,0]
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                continue
            dist = [[-1] * W for _ in range(H)]
            dist[h][w] = 0
            Q = deque([(h,w)])
            while Q:
                y, x = Q.popleft()
                for i in range(4):
                    nh = y + dh[i]
                    nw = x + dw[i]
                    if 0 <= nh < H and 0 <= nw < W and dist[nh][nw] == -1 and S[nh][nw] == '.':
                        dist[nh][nw] = dist[y][x] + 1
                        Q.append((nh,nw))
            for i in range(H):
                ans = max(ans, max(dist[i]))
                
    print(ans)



if __name__ == "__main__":
    main()