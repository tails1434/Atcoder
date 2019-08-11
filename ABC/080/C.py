N = int(input())

F = [[int(i) for i in input().split()] for i in range(N)]
P = [[int(i) for i in input().split()] for i in range(N)]

ans = - 10 ** 16
for i in range(1 << 10):
    output = [0] * 10
    for j in range(10):
        if (i>>j) & 1:
            output[j] = 1
    if output.count(0) == 10:
        continue
    tmp_sum = 0
    for n in range(N):
        cnt = 0
        for m in range(10):
            if F[n][m] == output[m] == 1:
                cnt += 1
        tmp_sum += P[n][cnt]
    ans = max(ans, tmp_sum)
print(ans)