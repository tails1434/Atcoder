from collections import deque

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    cnt = [[float('inf')] * W for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    Q = deque([])
    for h in range(H):
        for w in range(W):
            if C[h][w] == 's':
                cnt[h][w] = 0
                visited[h][w] = True
                Q.append([h,w])
            if C[h][w] == 'g':
                gh = h
                gw = w

    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    while Q:
        h, w = Q.popleft()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if nh == gh and nw == gw:
                print('YES')
                exit()
            if 0 <= nh < H and 0 <= nw < W:
                if not visited[nh][nw]:
                    if C[nh][nw] == '.':  
                        visited[nh][nw] = True
                        cnt[nh][nw] = min(cnt[nh][nw], cnt[h][w])
                        Q.append([nh,nw])
                    elif C[nh][nw] == '#':
                        if cnt[h][w] <= 1:
                            visited[nh][nw] = True
                            cnt[nh][nw] = min(cnt[nh][nw], cnt[h][w]+1)
                            Q.append([nh,nw])
                else:
                    if C[nh][nw] == '.':  
                        if cnt[nh][nw] > cnt[h][w]:
                            cnt[nh][nw] = min(cnt[nh][nw], cnt[h][w])
                            Q.append([nh,nw])
                    elif C[nh][nw] == '#':
                        if cnt[nh][nw] > cnt[h][w] + 1:
                            cnt[nh][nw] = min(cnt[nh][nw], cnt[h][w]+1)
                            Q.append([nh,nw])

    print('NO')
    

if __name__ == "__main__":
    main()