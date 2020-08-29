from collections import deque

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if C[h][w] == 's':
                sh = h
                sw = w
            if C[h][w] == 'g':
                gh = h
                gw = w

    dist = [[float('inf')] * W for _ in range(H)]
    dist[sh][sw] = 0
    Q = deque([[sh,sw]])
    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    while Q:
        h, w = Q.popleft()
        if h == gh and w == gw:
            break
        d = dist[h][w]
        if d >= 3:
            print('NO')
            exit()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]

            if 0 <= nh < H and 0 <= nw < W:
                if C[nh][nw] == "#":
                    if dist[nh][nw] > d:
                        dist[nh][nw] = d + 1
                        Q.append([nh,nw])
                else:
                    if dist[nh][nw] > d:
                        dist[nh][nw] = d
                        Q.appendleft([nh,nw])

    if dist[gh][gw] <= 2:
        print('YES')
    else:
        print('NO')
    



if __name__ == "__main__":
    main()