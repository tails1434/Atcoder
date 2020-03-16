from fractions import gcd
from functools import reduce


def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def func(x):
    return x // 2

def cont(x):
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    return cnt

def main():
    N, M = map(int, input().split())
    A = list(map(func, map(int, input().split())))

    l = lcm_list(A)
    cnt = cont(A[0])
    for i in range(1, N):
        if cnt != cont(A[i]):
            print(0)
            exit()

    ans = M // l
    if ans % 2 == 0:
        print(ans // 2)
    else:
        print(ans // 2 + 1)



if __name__ == "__main__":
    main()