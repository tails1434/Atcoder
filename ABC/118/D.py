def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    cost = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    dp = [-1] * (N + 10)
    dp[0] = 0
    sort_A = sorted(A, reverse=True)

    for a in sort_A:
        tmp = cost[a]
        for i in range(N + 1):
            if dp[i] == -1:
                continue
            dp[i+tmp] = max(dp[i+tmp], dp[i] * 10 + a)

    print(dp[N])






main()