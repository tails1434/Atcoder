def main():
    N, T = map(int, input().split())
    C = []
    max_A = 0
    for _ in range(N):
        A, B = map(int, input().split())
        max_A = max(max_A, A)
        C.append((A,B))

    C.sort()

    dp = [[0] * (T + max_A) for _ in range(N+5)]
    for i in range(N):
        for t in range(T):
            dp[i+1][t+C[i][0]] = max(dp[i+1][t+C[i][0]], dp[i][t] + C[i][1])
            dp[i+1][t] = max(dp[i+1][t], dp[i][t])        

    ans = 0
    for i in range(N+1):
        ans = max(ans, max(dp[i]))

    print(ans)


if __name__ == "__main__":
    main()