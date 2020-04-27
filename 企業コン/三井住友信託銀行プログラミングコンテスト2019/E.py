def main():
    MOD = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    d = [0] * (max(A) + 1)
    for a in A:
        if a == 0:
            ans *= 3 - d[a]
            ans %= MOD
            d[a] += 1
        else:
            ans *= d[a-1] - d[a]
            d[a] += 1
            ans %= MOD

    print(ans)



if __name__ == "__main__":
    main()