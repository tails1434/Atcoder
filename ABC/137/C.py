import collections
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N = int(input())

    s = [""] * N
    for i in range(N):
        s[i] = ''.join(sorted(input()))
    S = collections.Counter(s)
    
    cnt = 0
    for i in S.values():
        if i > 1:
            cnt += combinations_count(i, 2)

    print(cnt)
main()