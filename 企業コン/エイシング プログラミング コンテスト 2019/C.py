from collections import deque

def main():
    H, W = map(int, input().split())
    S = list(list(input()) for _ in range(H))
    visited = [[False] * W for _ in range(H)]
    blacks = []
    ans = 0
    dh = [0,1,0,-1]
    dw = [1,0,-1,0]
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                blacks.append((h,w))

    for h, w in blacks:
        if not visited[h][w]:
            Q = deque([(h,w)])
            white = 0
            black = 1
            visited[h][w] = True
            while Q:
                i, j = Q.popleft()
                now = S[i][j]

                for n in range(4):
                    nh = i + dh[n]
                    nw = j + dw[n]

                    if 0 <= nh < H and 0 <= nw < W:
                        if not visited[nh][nw]:
                            if now != S[nh][nw]:
                                visited[nh][nw] = True
                                Q.append((nh,nw))
                                if S[nh][nw] == '.':
                                    white += 1
                                else:
                                    black += 1
            ans += white * black

    print(ans)


if __name__ == "__main__":
    main()