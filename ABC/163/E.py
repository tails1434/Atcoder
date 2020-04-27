def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j] = A[i] * abs(i - j)

    print(dp)    


if __name__ == "__main__":
    main()