def main():
    N = int(input())
    dp = [[0] * 10 for _ in range(10)]
    for i in range(1,N+1):
        tmp = str(i)
        left = int(tmp[0])
        right = int(tmp[-1])
        if left == 0 or right == 0:
            continue
        dp[left][right] += 1

    ans = 0
    for i in range(10):
        for j in range(10):
            ans += dp[i][j] * dp[j][i]

    print(ans)


if __name__ == "__main__":
    main()