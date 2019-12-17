from fractions import gcd
from collections import defaultdict

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        tmp = gcd(K,a)
        d[tmp] += 1
    l = list(d.keys())
    ans = 0

    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] * l[j] % K == 0:
                if i == j:
                    ans += d[l[i]] * (d[l[i]] - 1)
                else:
                    ans += d[l[i]] * d[l[j]]

    ans //= 2
    print(ans)


if __name__ == "__main__":
    main()