from collections import defaultdict
def main():
    N = int(input())
    C = [int(input()) for _ in range(N)]
    MOD = 10 ** 9 + 7
    color = defaultdict(int)
    dp = [0] * (N+1)
    dp[0] = 1
    color[C[0]] = 0
    for i in range(1,N):
        if color.get(C[i]) == None or C[i] == C[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[color[C[i]]]
        color[C[i]] = i
        dp[i] %= MOD
    print(dp[N-1])


if __name__ == "__main__":
    main()