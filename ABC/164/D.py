from collections import defaultdict
def main():
    S = list(map(int,list(input())))
    N = len(S)
    M = [0] * (N + 1)
    ten = 1
    for i in range(N-1,-1,-1):
        M[i] = (S[i] * ten + M[i+1]) % 2019
        ten *= 10
        ten %= 2019

    d = defaultdict(int)

    for m in M:
        d[m] += 1
    ans = 0
    for i, j in d.items():
        ans += j * (j - 1) // 2
    
    print(ans)


if __name__ == "__main__":
    main()