N, K = map(int, input().split())
A = list(map(int, input().split()))

TMP = [0] * N

for i in A:
    TMP[i-1] += 1

filter_TMP = sorted([i for i in TMP if i > 0], reverse=True)

max_ball = 0
cnt = 1
for i in filter_TMP:
    if cnt <= K:
        max_ball += i
        cnt += 1
    else:
        break
    

print(N - max_ball)