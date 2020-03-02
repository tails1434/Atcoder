def main():
    N, M = map(int, input().split())
    S = []
    for i in range(M):
        a, b = map(int, input().split())
        C = list(map(int, input().split()))
        s = 0
        for c in C:
            c -= 1
            s |= (1 << c)
        S.append((a,s))

    dp = [float('inf')] * (1 << N)
    dp[0] = 0
    for i in range(1 << N):
        for j in range(M):
            t = i | S[j][1]
            dp[t] = min(dp[t], dp[i] + S[j][0])

    if dp[(1<<N)-1] == float('inf'):
        print(-1)
    else:
        print(dp[(1<<N)-1])
    
if __name__ == "__main__":
    main()