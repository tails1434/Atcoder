def main():
    N = int(input())

    #dp = [[[[0] * 4] * 4] * 4 for _ in range(N + 1)]
#
    #dp[0][3][3][3] = 1
    #MOD = 10**9+7
#
    #for n in range(N):
    #    for i in range(4):
    #        for j in range(4):
    #            for k in range(4):
    #                if dp[n][i][j][k] == 0:
    #                    continue
    #                
    #                for a in range(4):
    #                    if j == 0 and i == 1 and a == 2:
    #                        continue
    #                    if j == 1 and i == 0 and a == 2:
    #                        continue
    #                    if j == 0 and i == 2 and a == 1:
    #                        continue
    #                    if k == 0 and i == 1 and a == 2:
    #                        continue
    #                    if k == 0 and j == 1 and a == 2:
    #                        continue
#
    #                    dp[n+1][j][i][a] += dp[n][k][j][i]
    #                    dp[n+1][j][i][a] %= MOD
#
#
    #ans = 0
    #for i in range(4):
    #        for j in range(4):
    #            for k in range(4):
    #                ans += dp[N][k][j][i]
    #                ans %= MOD
#
    #print(ans)
    dp = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(101)]
    dp[0][3][3][3] = 1

    mod = 10**9+7

    #文字列の文字数
    for len in range(N):
        #最後から1文字目の文字
        for c1 in range(4):
            #最後から2文字目の文字
            for c2 in range(4):
                #最後から3文字目の文字
                for c3 in range(4):
                    #新しく追加する文字
                    for a in range(4):
                        if c2 == 0 and c1 == 1 and a == 2 : #012
                            continue
                        if c2 == 1 and c1 == 0 and a == 2 : #102
                            continue
                        if c2 == 0 and c1 == 2 and a == 1 : #021
                            continue
                        if c3 == 0 and c1 == 1 and a == 2 : #0?12
                            continue
                        if c3 == 0 and c2 == 1 and a == 2 : #01?2
                            continue

                        dp[len + 1][c2][c1][a] += dp[len][c3][c2][c1]

    ans = 0

    #最後から1文字目の文字
    for c1 in range(4):
        #最後から2文字目の文字
        for c2 in range(4):
            #最後から3文字目の文字
            for c3 in range(4): 
                ans += dp[N][c3][c2][c1]
                ans %= mod

    print(ans)


main()