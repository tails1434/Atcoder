def main():
    N = int(input())
    P = list(map(int, input().split()))
    dp = [0] * (sum(P) + 5)
    dp[0] = 1
    for p in P:
        # 前からスタートすると自分自身を延々とカウントしてしまうので後ろから計算する
        # 2の場合を考えると
        # 0 => 2 => 4 ・・・・のような感じ
        for i in range(sum(P) + 1, -1, -1):
            if dp[i] == 1 and i + p <= sum(P):
                dp[i + p] = 1

    print(dp.count(1))

if __name__ == "__main__":
    main()