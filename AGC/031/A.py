from collections import Counter
def main():
    N = int(input())
    S = list(input())
    MOD = 10 ** 9 + 7
    C = Counter(S)
    ans = 1
    for c in C.values():
        ans *= (c+1)
        ans %= MOD

    print(ans - 1)


    

if __name__ == "__main__":
    main()