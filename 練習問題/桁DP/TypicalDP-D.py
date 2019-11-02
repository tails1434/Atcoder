def main():
    D = int(input())
    N = str(input())

    MOD = 10 ** 9 + 7
    L = len(N)

    dp = [[[0] * 2 for _ in range(D)] for _ in range(L + 1)]
    dp[0][0][0] = 1

    for i in range(L):
        num = int(N[i])
        for j in range(2):
            # kは各桁の和の%modを表す
            for k in range(D):
                # j = 1のときは何でも(0～9)選んで良いので10
                # j = 0のときはNの値までしか選べないのでnum+1とする
                for d in range(10 if j else num + 1):
                    # j or (d < num)はjが1のときは1で
                    # j = 0の場合はd < numがTrueの場合1でFalse(d=num)の場合0になる
                    dp[i+1][(k + d) % D][j or (d < num)] += dp[i][k][j]
                    dp[i+1][(k + d) % D][j or (d < num)] %= MOD
    
    # 答えはすべての桁の値が0のときを除くから1引く 
    print(dp[L][0][1] + dp[L][0][0] - 1)

main()