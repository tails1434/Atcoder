def main():
    N = int(input())

    dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(N + 2)]
    '''
    A => 0
    C => 1
    G => 2
    T => 3
    '''
    MOD = 10 ** 9 + 7
    dp[0][3][3][3] = 1
    for i in range(N):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    for a in range(4):
                    
                        if c2 == 0 and c3 == 1 and a == 2:
                            continue
                        if c2 == 1 and c3 == 0 and a == 2:
                            continue
                        if c2 == 0 and c3 == 2 and a == 1:
                            continue
                        if c1 == 0 and c3 == 1 and a == 2:
                            continue
                        if c1 == 0 and c2 == 1 and a == 2:
                            continue

                        dp[i+1][c2][c3][a] += dp[i][c1][c2][c3]

    ans = 0
    for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    ans += dp[N][c1][c2][c3]
                    ans %= MOD

    print(ans)
    
main()