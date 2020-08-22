
def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if (h % 2 == 0 and w % 2 == 1) or (h % 2 == 1 and w % 2 == 0):
                C[h][w] = -C[h][w]
    S = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            S[h+1][w+1] = S[h][w+1] + S[h+1][w] - S[h][w] + C[h][w]
    ans = 0
    for h1 in range(H+1):
        for w1 in range(W+1):
            for h2 in range(h1+1,H+1):
                for w2 in range(w1+1,W+1):
                    if (S[h2][w2]-S[h1][w2]-S[h2][w1]+S[h1][w1]) == 0:
                        tmp = (h2-h1) * (w2-w1)
                        ans = max(ans, tmp)
    print(ans)
if __name__ == "__main__":
    main()