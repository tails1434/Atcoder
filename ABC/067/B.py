N, K = map(int, input().split())
l = list(map(int, input().split()))

sort_l = sorted(l, reverse=True)

cnt = 0
sum = 0
while cnt < K:
    sum += sort_l[cnt]
    cnt += 1
print(sum)