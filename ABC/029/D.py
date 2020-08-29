def main():
    N = input()
    dp = [[[0] * 2 for _ in range(11)] for _ in range(len(N)+1)]
    dp[0][0][0] = 1

    for i in range(len(N)):
        for j in range(10):
            # 1を選ぶ場合
            dp[i+1][j+1][1] += dp[i][j][1]
            # 1以外を選ぶ場合
            dp[i+1][j][1] += 9 * dp[i][j][1]
            if N[i] == '1':
                # 1を選ぶ場合
                dp[i+1][j+1][0] += dp[i][j][0]
                # 0を選ぶ場合
                dp[i+1][j][1] += dp[i][j][0]
            elif N[i] == '0':
                # 0を選ぶ場合
                dp[i+1][j][0] += dp[i][j][0]
            # 2 <= N[i] <= 9
            else:
                # N[i]の場合
                dp[i+1][j][0] += dp[i][j][0]
                # 1を選ぶ場合
                dp[i+1][j+1][1] += dp[i][j][0]
                # N[i]以下のその他の数を選ぶ場合
                dp[i+1][j][1] += (int(N[i]) - 1) * dp[i][j][0]

    ans = 0
    for j in range(11):
        for k in range(2):
            ans += j * dp[len(N)][j][k]
    print(ans)



if __name__ == "__main__":
    main()