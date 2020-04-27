def main():
    n, a, b = map(int, input().split())
    c = 1
    d = 1
    MOD = 10 ** 9 + 7
    for i in range(a):
        c *= n - i
        d *= i + 1
        c %= MOD
        d %= MOD

    nca = c * pow(d, MOD - 2, MOD)
    nca %= MOD

    c = 1
    d = 1
    for i in range(b):
        c *= n - i
        c %= MOD
        d *= i + 1
        d %= MOD

    ncb = c * pow(d, MOD - 2, MOD)
    ncb %= MOD
    ans = pow(2, n, MOD)
    ans -=  nca + ncb
    ans %= MOD
    print(ans-1)

if __name__ == "__main__":
    main()