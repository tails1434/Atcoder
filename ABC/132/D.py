import math

def comb(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

def main():
    MOD = 10 ** 9 + 7
    N, K = map(int, input().split())
    for i in range(1,K+1):
        if i > N - K + 1:
            print(0)
            continue
        blue = comb(N-K+1,i) % MOD
        red = comb(K-1,i-1) % MOD

        ans = blue * red % MOD

        print(ans)
            

main()