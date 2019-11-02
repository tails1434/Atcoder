def calc(A):
    # 10 ** 12 <= 2進数 40桁くらい
    A += 1
    cnt = 0
    ans = 0
    # i桁目の偶奇を調べる
    for i in range(50):
        # 0桁目 => 周期2 0,1,0,1
        # 1桁目 => 周期4 0,0,1,1,0,0,1,1
        # 2桁目 => 周期8 0,0,0,0,1,1,1,1
        loop = pow(2,i+1)

        # まず割り切れる部分のみを計算する
        cnt = (A // loop) * (loop // 2)

        # 端数部分を計算する
        if (A % loop) - (loop // 2) > 0:
            cnt += (A % loop) - (loop // 2)
        
        # 計算した桁数の1の数が奇数だったら足し算
        if cnt % 2 == 1:
            ans += 1 << i
    return ans


def main():
    A, B = map(int, input().split())

    print(calc(A-1)^calc(B))


main()