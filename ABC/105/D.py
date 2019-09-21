from collections import defaultdict

from operator import mul
from functools import reduce
 
def cmb(n,r):
    if n < r:
        return 0
    r = min(n-r,r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N+1)

    for i in range(1,N+1):
        sum_A[i] = (sum_A[i-1] + A[i-1]) % M
        
    ans = 0
    d = defaultdict(int)
    for i in range(N+1):
        d[sum_A[i]] += 1

    for i,j in d.items():
        ans += cmb(j,2)

    print(ans)

main()