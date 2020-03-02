from fractions import gcd
from functools import reduce

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def cnt_div_2(x):
    cnt = 0
    while x > 0:
        if x % 2 == 0:
            x //= 2
            cnt += 1
        else:
            break
    return cnt

def main():
    N, M = map(int, input().split())
    A = list(set(map(int, input().split())))
    cnt_2 = cnt_div_2(A[0])
    for a in A:
        if cnt_div_2(a) != cnt_2:
            print(0)
            exit()


    common = lcm_list(A)
    max_A = max(A)
    cnt = M // common
    if ((2 * cnt + 1) * common) // 2 <= M:
        print(cnt + 1)
    else:
        print(cnt)
    
if __name__ == "__main__":
    main()