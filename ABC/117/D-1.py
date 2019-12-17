def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    MAX_DIGIT = 45
    dp = [[-1] * 2 for _ in range(MAX_DIGIT+1)]
    dp[45][0] = 0
    for d in range(MAX_DIGIT-1,-1,-1):
        mask = 1 << d
        num = 0
        for i in range(N):
            if A[i] & mask:
                num += 1
        
        zero = mask * num
        one = mask * (N - num)

        if dp[d+1][1] != -1:
            dp[d][1] = max(dp[d][1], dp[d+1][1] + max(one, zero))

        if dp[d+1][0] != -1:
            if K & mask:
                dp[d][1] = max(dp[d][1], dp[d+1][0] + zero)
                dp[d][0] = max(dp[d][0], dp[d+1][0] + one)
            else:
                dp[d][0] = max(dp[d][0], dp[d+1][0] + zero)

    print(max(dp[0][0],dp[0][1]))


if __name__ == "__main__":
    main()