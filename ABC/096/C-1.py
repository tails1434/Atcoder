def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]

    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    for h in range(H):
        for w in range(W):
            if S[h][w] == '#':
                flag = False
                for i in range(4):
                    ny = h + dy[i]
                    nx = w + dx[i]

                    if 0 <= ny < H and 0 <= nx < W:
                        if S[ny][nx] == '#':
                            flag = True
                if not flag:
                    print('No')
                    exit()

    print('Yes')
    

main()