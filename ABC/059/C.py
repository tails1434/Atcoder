# 最初はa[0]がプラス、マイナスで場合分けしていたが、それだと最小にならない可能性があるため
# 偶数番目の和をプラス、奇数番目の和をプラスにする場合をやって最小になるほうを結果として出す

n = int(input())
a = list(map(int, input().split()))

cnt = [0,0]

for i in [0,1]:
    tmp_sum = 0
    for index, value in enumerate(a):
        tmp_sum += value
        if (i + index) % 2 == 0:
            if tmp_sum <= 0:
                cnt[i] += abs(tmp_sum) + 1
                tmp_sum += abs(tmp_sum) + 1
        else:
            if tmp_sum >= 0:
                cnt[i] += tmp_sum + 1
                tmp_sum -= tmp_sum + 1


print(min(cnt))