def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    MAX_DIGIT = 50

    # dp[桁数][0 or 1] 
    # 0: Kより小さいことが未確定
    # 1: Kより小さいことが確定
    dp = [[-1] * 2 for _ in range(MAX_DIGIT+5)]
    dp[0][0] = 0

    for d in range(MAX_DIGIT):
        # d桁目にビットが立っているか調べるためmaskを作る
        # 例) 6桁目のビットを調べたい場合 mask = 100000
        mask = 1 << (MAX_DIGIT - d - 1)

        # A で元々d桁目にビットが立っている個数
        num = 0
        for i in range(N):
            # maskはd桁目のみ1となっているので
            # 調べたい対象の数字のd桁目が1の場合のみ(A[i] & mask) != 0となる
            if A[i] & mask:
                num += 1
        
        # Xのd桁目を0,1にしたときのスコア
        score0 = mask * num
        score1 = mask * (N - num)

        # 1 => 1への遷移
        # score0 or score1の大きい方を選択可能
        if dp[d][1] != -1:
            dp[d+1][1] = max(dp[d+1][1], dp[d][1] + max(score0, score1))

        # 0 => 1への遷移
        # Kのd桁目が1の時、Xのd桁目を0にする場合
        if dp[d][0] != -1:
            if K & mask:
                dp[d+1][1] = max(dp[d+1][1], dp[d][0] + score0)
        
        # 0 => 0への遷移
        # Kのd桁目が1の時、Xのd桁目を1
        # Kのd桁目が0の時、Xのd桁目を0にする場合
        if dp[d][0] != -1:
            if K & mask:
                dp[d+1][0] = max(dp[d+1][0], dp[d][0] + score1)
            else:
                dp[d+1][0] = max(dp[d+1][0], dp[d][0] + score0)

    print(max(dp[MAX_DIGIT][0],dp[MAX_DIGIT][1]))

main()