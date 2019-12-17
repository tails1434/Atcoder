from collections import defaultdict
from itertools import accumulate
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    d = defaultdict(list)
    for _ in range(N):
        t, v = map(int, input().split())
        d[t].append(v)

    other = []
    vmax = []
    for nums in d.values():
        nums.sort(reverse=True)
        for i, j in enumerate(nums):
            if i == 0:
                vmax.append(j)
            else:
                other.append(j)

    vmax.sort(reverse=True)
    other.sort(reverse=True)
    sum_v = [0] + list(accumulate(vmax))
    sum_o = [0] + list(accumulate(other))
    ans = 0
    for i in range(K,0,-1):
        neta = min(i, len(vmax))
        base = neta * neta
        tmp = base + sum_v[neta]
        if K - neta > len(other):
            break
        tmp += sum_o[K-neta]
        ans = max(ans, tmp)
        


    print(ans)

    
    




if __name__ == "__main__":
    main()