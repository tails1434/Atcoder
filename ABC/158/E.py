from itertools import accumulate
from collections import defaultdict

def main():
    N, P = map(int, input().split())
    S = list(map(int, list(input())))
    ans = 0
    if P == 2:
        for i in range(N-1,-1,-1):
            if S[i] % 2 == 0:
                ans += i + 1
        print(ans)
        exit()
    if P == 5:
        for i in range(N-1,-1,-1):
            if S[i] % 5 == 0:
                ans += i + 1
        print(ans)
        exit()
    
    ten = 1
    d = defaultdict(int)
    C = [0] * (N + 1)
    for i in range(N-1,-1,-1):
        tmp = (S[i] * ten) % P
        idx = N - 1 - i
        C[idx + 1] = (C[idx] + tmp) % P
        ten *= 10
        ten %= P
    print(C)
    for c in C:
        d[c] += 1
    print(d)
    for i, j in d.items():
        ans += j * (j - 1) // 2

    print(ans)    


if __name__ == "__main__":
    main()