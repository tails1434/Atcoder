from math import factorial
import itertools

N = int(input())

C = [int(input()) for i in range(N)]

ans = 0

for c in C:
    # 必ず自分自身が約数として含まれるため-1からスタートする
    cnt = -1
    for b in C:
        if c % b == 0:
            cnt += 1
    if cnt % 2 == 0:
        ans += (cnt + 2) / ( 2 * cnt + 2)
    else:
        ans += 0.5
            
print(ans)