from fractions import gcd
from functools import reduce


def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    D = lcm_list(A)
    ans = 0
    MOD = 10 ** 9 + 7
    D %= MOD
    for a in A:
        ans += D * pow(a, MOD - 2, MOD)
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
