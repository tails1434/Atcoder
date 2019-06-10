N, M = map(int, input().split())
a = set(int(input()) for i in range(M))

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1,N+1):
    if i in a:
        dp[i] = 0
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[N])