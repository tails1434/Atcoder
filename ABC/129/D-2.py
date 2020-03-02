def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    L = [[0] * W for _ in range(H)]
    R = [[0] * W for _ in range(H)]    
    T = [[0] * W for _ in range(H)]
    D = [[0] * W for _ in range(H)]

    for h in range(H):
        cnt = 1
        for w in range(W):
            if S[h][w] == '#':
                cnt = 1
            else:
                L[h][w] = cnt
                cnt += 1

    for h in range(H):
        cnt = 1
        for w in range(W-1,-1,-1):
            if S[h][w] == '#':
                cnt = 1
            else:
                R[h][w] = cnt
                cnt += 1

    for w in range(W):
        cnt = 1
        for h in range(H):
            if S[h][w] == '#':
                cnt = 1
            else:
                T[h][w] = cnt
                cnt += 1

    for w in range(W):
        cnt = 1
        for h in range(H-1,-1,-1):
            if S[h][w] == '#':
                cnt = 1
            else:
                D[h][w] = cnt
                cnt += 1

    ans = 0
    for h in range(H):
        for w in range(W):
            tmp = T[h][w] + D[h][w] + L[h][w] + R[h][w] - 3
            ans = max(ans, tmp)

    print(ans)

if __name__ == "__main__":
    main()