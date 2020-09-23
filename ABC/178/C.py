def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    ans = pow(10,N,MOD) - (2 * pow(9,N,MOD) - pow(8,N,MOD))
    ans %= MOD
    print(ans)



if __name__ == "__main__":
    main()