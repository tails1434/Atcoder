import sys
from functools import lru_cache
 
sys.setrecursionlimit(4100000)
 
@lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 0

    return f(n % bin(n).count('1')) + 1

def main():
    N = int(input())
    X = list(input())
    pc = X.count('1')
    now = 0
    for i in range(N):
        if X[i] == '1':
            now += pow(2,N-i-1)

    ac = pc + 1
    dc = pc - 1
    # ここの処理が速さに相当効く
    ac_now = now % ac
    if dc:
        dc_now = now % dc
    for i in range(N):
        cnt = 0
        if X[i] == '1' and dc:
            tmp = (dc_now - pow(2, N-i-1, dc)) % dc
            cnt = 1 + f(tmp)
        elif X[i] == '0':
            tmp = (ac_now + pow(2, N-i-1, ac)) % ac
            cnt = 1 + f(tmp)

        print(cnt)



if __name__ == "__main__":
    main()