def main():
    H, W = map(int, input().split())
    S = list(input() for _ in range(H))

    left = [[0] * W for _ in range(H)]
    right = [[0] * W for _ in range(H)]
    up = [[0] * W for _ in range(H)]
    down = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j-1] + 1

    for i in range(H):
        for j in range(W-1,-1,-1):
            if S[i][j] == '.':
                if j == W-1:
                    right[i][j] = 1
                else:
                    right[i][j] = right[i][j+1] + 1

    for j in range(W):
        for i in range(H):
            if S[i][j] == '.':
                if i == 0:
                    down[i][j] = 1
                else:
                    down[i][j] = down[i-1][j] + 1

    for j in range(W):
        for i in range(H-1,-1,-1):
            if S[i][j] == '.':
                if i == H - 1:
                    up[i][j] = 1
                else:
                    up[i][j] = up[i+1][j] + 1

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            ans = max(ans, left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3)

    print(ans)

main()