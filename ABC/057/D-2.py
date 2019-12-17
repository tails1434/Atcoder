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
    ave = 0
    for i in range(A):
        ave += sort_v[i]
    ave = ave / A
    ans = 0
    if sort_v[0] == sort_v[A-1]:
        cnt = v.count(sort_v[A-1])
        for i in range(A, min(cnt,B)+1):
            ans += cmb(cnt,i)
    else:
        cnt = v.count(sort_v[A-1])
        ind = sort_v.index(sort_v[A-1])
        ans = cmb(cnt, A - ind)
    print(ave)
    print(ans)


if __name__ == "__main__":
    main()