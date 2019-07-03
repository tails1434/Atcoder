import math
from collections import defaultdict

N = int(input())

d = defaultdict(int)

def division(n,d):
    flag = True
    tmp = n // 2 + 1
    for num in range(2, tmp):
        while n % num == 0:
            flag = False
            n //= num
            d[num] += 1

    if flag:
        d[n] += 1

    return

for n in range(2,N+1):
    division(n,d)

ans = 1
for i in d.values():
    ans *= (i+1)

print(ans%(10**9+7))

