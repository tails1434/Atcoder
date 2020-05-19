def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    left = [[0] * W for _ in range(H)]
    right = [[0] * W for _ in range(H)]
    up = [[0] * W for _ in range(H)]
    down = [[0] * W for _ in range(H)]
    for i in range(H):
        cnt = 0
        for j in range(W):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
            left[i][j] = cnt
    
    for i in range(H):
        cnt = 0
        for j in range(W-1,-1,-1):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
            right[i][j] = cnt
    
    for j in range(W):
        cnt = 0
        for i in range(H):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
            up[i][j] = cnt
    
    for j in range(W):
        cnt = 0
        for i in range(H-1,-1,-1):
            if S[i][j] == '#':
                cnt = 0
            else:
                cnt += 1
            down[i][j] = cnt
    
    ans = 0
    for i in range(H):
        for j in range(W):
            tmp = up[i][j] + down[i][j] + left[i][j] + right[i][j] - 3
            ans = max(ans, tmp)


    print(ans)
    


if __name__ == "__main__":
    main()