def main():
    W = int(input())
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    dp = [[0] * (K + 1) for _ in range(W + 1)]

    for i in range(1,N+1):
        for w in range(W,-1,-1):
            for k in range(K+1):
                if i == 0 or k == 0:
                    dp[w][k] = 0
                elif w >= A[i-1]:
                    dp[w][k] = max(dp[w][k], dp[w-A[i-1]][k-1] + B[i-1])

    print(dp[W][K])

if __name__ == "__main__":
    main()