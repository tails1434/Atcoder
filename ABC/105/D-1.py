from itertools import accumulate
from collections import defaultdict
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(accumulate(A))
    d = defaultdict(int)
    for i in range(N):
        B[i] %= M
        d[B[i]] += 1

    cnt = 0
    for i, j in d.items():
        if i == 0:
            cnt += j
        if j >= 2:
            cnt += cmb(j , 2)

    print(cnt)
    
    
            
        
if __name__ == "__main__":
    main()