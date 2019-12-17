# M = a ** x * b ** y * c ** z
# の約数の個数は(x + 1)*(y + 1)*(z + 1)
# なので約数が75個になるには、以下パターンが考えられる
# 75
# 25 * 3
# 15 * 5
# 5 * 5 * 3
# よって1～Nまで素因数分解して、各素因数の指数部分の値を求めて
# 計算する

import itertools

def main():
    N = int(input())
    d = [0] * (N+1)

    for i in range(2,N+1):
        cur = i
        for j in range(2, i+1):
            while cur % j == 0:
                d[j] += 1
                cur = cur // j

    print(d)
    ans = 0
    for i in d:
        if i >= 74:
            ans += 1
    for (x, y, z) in itertools.combinations(d,3):
        for a, b, c in [[4, 4, 2],[4, 2, 4],[2, 4, 4]]:
            if x >= a and y >= b and z >= c:
                ans += 1

    for (x, y) in itertools.combinations(d,2):
        for a, b in [[24,2],[14,4],[4,14],[2,24]]:
            if x >= a and y >= b:
                ans += 1

    print(ans)


    

main()