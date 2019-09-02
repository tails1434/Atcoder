import sys
sys.setrecursionlimit(10000000)
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(i,cost):
    if i == N:
        return 0

    res1 = dfs(i+1,cost)
    res2 = dfs(i+1,cost+C[i]) + V[i] - C[i]

    return max(res1,res2)

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

print(dfs(0,0))