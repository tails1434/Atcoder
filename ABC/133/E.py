import sys
from math import factorial
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        if n < r:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    # 階乗
    def fact(self, n):
        return self.fac[n] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

comb = Combination(10 ** 5 + 5)
MOD = 10 ** 9 + 7

def permutations_count(n, r):
    return (comb(n,r) * comb.fact(r)) % MOD

def main():
    N, K = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    ans = 1
    q = deque([])
    q.append((0,-1))
    while q:
        s, p = q.popleft()
        for v in edge[s]:
            if p == v:
                continue
            q.append((v,s))
        nk = K if p == -1 else K - 2
        # edge[s]には親が含まれているため-1する必要がある
        c = len(edge[s]) + 1 if p == -1 else len(edge[s]) - 1
        ans *= permutations_count(nk,c)
        ans %= MOD

    

    print(ans)


    
if __name__ == "__main__":
    main()