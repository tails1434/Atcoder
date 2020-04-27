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
    MOD = 10 ** 9 + 7
    com = lcm_list(A) % MOD
    ans = 0
    for a in A:
        ans += com * pow(a, MOD - 2, MOD)
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()