
def main():
    n, a, b = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = pow(2, n, MOD)
    e = 1
    f = 1
    for i in range(1,a+1):
        e *= (n - i + 1)
        f *= i 
        e %= MOD
        f %= MOD
    c = e * pow(f, MOD-2, MOD)
    e = 1
    f = 1
    for i in range(1,b+1):
        e *= (n - i + 1)
        f *= i 
        e %= MOD
        f %= MOD
    d = e * pow(f, MOD-2, MOD)
    ans -= (c + d)
    ans %= MOD
    print(ans-1)



if __name__ == "__main__":
    main()