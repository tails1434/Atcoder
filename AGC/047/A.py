from collections import Counter
from decimal import Decimal

def func(n):
    cnt2 = 0
    cnt5 = 0
    while n % 2 == 0:
        n //= 2
        cnt2 += 1
    while n % 5 == 0:
        n //= 5
        cnt5 += 1
    return cnt2, cnt5

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    ctr = Counter()

    for a in A:
        d = Decimal(a)
        d = int(d * 1000000000)
        cnt2, cnt5 = func(d)
        ctr[(cnt2,cnt5)] += 1
    ans = 0
    for (ni1, go1), v1 in ctr.items():
        for (ni2, go2), v2 in ctr.items():
            if not (ni1 + ni2 >= 18 and go1 + go2 >= 18):
                continue
            if ni1 == ni2 and go1 == go2:
                ans += v1 * (v1 - 1)
            else:
                ans += v1 * v2


    print(ans // 2)


if __name__ == "__main__":
    main()