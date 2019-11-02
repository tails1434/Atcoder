def main():
    H, W = map(int, input().split())
    S = list(input() for _ in range(H))

    L = [[0] * W for _ in range(H)]
    R = [[0] * W for _ in range(H)]
    U = [[0] * W for _ in range(H)]
    D = [[0] * W for _ in range(H)]

    # Lをカウント
    for i in range(H):
        cnt = 0
        for j in range(W):
            if S[i][j] == '#':
                cnt = 0
                continue
            else:
                cnt += 1
                L[i][j] = cnt

    for i in range(H):
        cnt = 0
        for j in range(W-1, -1, -1):
            if S[i][j] == '#':
                cnt = 0
                continue
            else:
                cnt += 1
                R[i][j] = cnt

    for j in range(W):
        cnt = 0
        for i in range(H):
            if S[i][j] == '#':
                cnt = 0
                continue
            else:
                cnt += 1
                U[i][j] = cnt

    for j in range(W):
        cnt = 0
        for i in range(H-1,-1,-1):
            if S[i][j] == '#':
                cnt = 0
                continue
            else:
                cnt += 1
                D[i][j] = cnt

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            tmp = L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3
            ans = max(ans,tmp)

    print(ans)

main()