from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
    N, A, B = map(int, input().split())
    v = list(map(int, input().split()))
    sort_v = sorted(v, reverse=True)
    sum_A = 0
    for i in range(A):
        sum_A += sort_v[i]
    max_ave_v = sum_A / A

    print(max_ave_v)

    num = sort_v.count(sort_v[0])
    num2 = sort_v.count(sort_v[A-1])
    if sort_v[0] == sort_v[A-1]:
        ans = 0
        for i in range(A,B+1):
            if num >= i:
                ans += cmb(num,i)
    else:
        cnt = 0
        for i in range(A):
            if sort_v[i] == v[A-1]:
                cnt += 1
        ans = cmb(num2, cnt)

    print(ans)
        


main()