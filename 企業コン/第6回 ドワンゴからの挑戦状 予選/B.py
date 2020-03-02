from math import factorial

def main():
    N = int(input())
    X = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    diff = [0] * (N - 1)
    for i in range(N-1):
        diff[i] = X[i+1] - X[i]
    
    ans = 0
    cnt = factorial(N - 1)


    for i in range(N-1):
        ans += (diff[i] % MOD ) * (cnt % MOD)
        #ans %= MOD
        cnt += (i + 1) * (cnt // factorial(i + 2))
        #cnt %= MOD
    
    print(ans % MOD)

if __name__ == "__main__":
    main()