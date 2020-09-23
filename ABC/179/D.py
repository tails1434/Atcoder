
def main():
    N, K = map(int, input().split())
    MOD = 998244353
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())

    
    dp = [0] * (N + 1)
    dpsum = [0] * (N + 1)
    dp[1] = 1
    dpsum[1] = 1
    for i in range(2,N+1):
        for j in range(K):
            l = i - R[j]
            r = i - L[j]
            if r <= 0:
                continue
            l = max(1,l)
            dp[i] += dpsum[r] - dpsum[l-1]
            dp[i] %= MOD
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= MOD

    print(dp[N])


if __name__ == "__main__":
    main()
