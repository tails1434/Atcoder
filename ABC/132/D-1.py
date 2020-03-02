from operator import mul
from functools import reduce

def cmb(n,r):
    if n < r: return 0
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    for i in range(1,K+1):
        if N - K + 1 < i:
            print(0)
            continue
        blue = cmb(K-1,i-1)
        red = cmb(N-K+1,N-K-i+1)
        ans = blue * red
        ans %= MOD
        print(ans)
        


if __name__ == "__main__":
    main()