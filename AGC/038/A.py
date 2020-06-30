def main():
    H, W, A, B = map(int, input().split())
    S = [[0] * W for _ in range(H)]
    for i in range(B):
        for j in range(W):
            if j >= A:
                S[i][j] = 1

    for i in range(A):
        for j in range(H):
            if j >= B:
                S[j][i] = 1

    for i in range(H):
        print(*S[i], sep='')




if __name__ == "__main__":
    main()