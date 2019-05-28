import sys
sys.setrecursionlimit(1000000)

def tri(n):
    memo = [0] * n #n個の要素がある配列を用意
    memo[0:3] = [0,0,1] # 用意した配列に代入 [0,0,1,0,0,0,0・・・・]という感じになる
    for i in range(3, n): # for文を3からスタートで行う。
        memo[i] = (memo[i-1] + memo[i-2] + memo[i-3]) % 10007
    return memo[n-1]

N = int(input())

print(tri(N))