def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    C = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            C[h][w] = abs(A[h][w] - B[h][w])

    dp = [[0 for _ in range(6400)] for _ in range(H*W)]
    dp[0][C[0][0]] = 1

    for d in range(H*W):
        h, w = divmod(d, W)
        for k in range(6400):
            if not dp[h*W+w][k]:
                continue
            nh, nw = h+1, w+1
            if nh < H:
                if k + C[nh][w] < 6400:
                    dp[nh*W+w][k+C[nh][w]] = 1
                dp[nh*W+w][abs(k-C[nh][w])] = 1
            if nw < W:
                if k + C[h][nw] < 6400:
                    dp[h*W+nw][k+C[h][nw]] = 1
                dp[h*W+nw][abs(k-C[h][nw])] = 1

    for k in range(6400):
        if dp[-1][k]:
            print(k)
            exit()

if __name__ == "__main__":
    main()