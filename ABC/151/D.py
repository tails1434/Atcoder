from collections import deque

def main():
    H, W = map(int, input().split())
    S = list(input() for _ in range(H))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def bfs(h,w):
        Q = deque([(h,w)])
        dist = [[-1] * W for _ in range(H)]
        dist[h][w] = 0
        while Q:
            y, x = Q.popleft()

            for i in range(4):
                nh = y + dy[i]
                nw = x + dx[i]

                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == float(-1):
                    dist[nh][nw] = dist[y][x] + 1
                    Q.append((nh,nw))

        tmp = 0
        for a in range(H):
            tmp = max(tmp, max(dist[a]))
        return tmp
    
    ans = []
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans.append(bfs(h,w))
    

    print(max(ans))


    

if __name__ == "__main__":
    main()