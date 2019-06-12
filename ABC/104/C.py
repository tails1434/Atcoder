D, G = map(int, input().split())
p = [0] * D
c = [0] * D

for i in range(D):
    p[i], c[i] = map(int, input().split())

ans = float('inf')

for i in range(1<<D):
    tmp_score = 0
    cnt = 0
    max_value = -1
    for j in range(D):
        if (i >> j) & 1 == 1:
            tmp_score += 100 * (j + 1) * p[j] + c[j]
            cnt += p[j]
        else:
            max_value = j

    if tmp_score < G:
        for k in range(1,p[max_value]):
            tmp_score += 100 * (max_value + 1)
            cnt += 1
            if tmp_score >= G:
                break
    
    if tmp_score >= G:
        if ans > cnt:
            ans = cnt

print(ans)
