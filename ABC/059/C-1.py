n = int(input())
A = list(map(int, input().split()))

cnt = [0,0]

for i in [0,1]:
    tmp_sum = 0
    for j, a in enumerate(A):
        tmp_sum += a
        if (i + j) % 2 == 0 and tmp_sum <= 0:
            cnt[i] += abs(tmp_sum) + 1
            tmp_sum += abs(tmp_sum) + 1
        elif (i + j) % 2 == 1 and tmp_sum >= 0:
            cnt[i] += tmp_sum + 1
            tmp_sum -= tmp_sum + 1

print(min(cnt))
            