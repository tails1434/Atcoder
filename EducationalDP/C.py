def main():
    N = int(input())
    work = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        work.append((a,b,c))
    
    dp = [[0] * 3 for _ in range(N)]
    for i in range(N):
        for j in range(3):
            if i == 0:
                dp[i][j] = work[i][j]
                continue
            if j == 0:
                dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + work[i][0]
            elif j == 1:
                dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + work[i][1]
            elif j == 2:
                dp[i][2] = max(dp[i-1][1], dp[i-1][0]) + work[i][2]

    print(max(dp[N-1]))
    

if __name__ == "__main__":
    main()