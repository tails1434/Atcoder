from collections import defaultdict
from bisect import bisect_right

def main():
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        s = int(input())
        d[s] += 1
    pre = -1
    key = list(sorted(d.keys(),reverse=True))
    value = [0] * len(key)
    for i, j in enumerate(key):
        d[j] += d[pre]
        pre = j
        value[i] = d[j]
    Q = int(input())
    for _ in range(Q):
        k = int(input())
        if k == N:
            print(0)
            continue
        a = bisect_right(value, k)
        if key[a] == 0:
            print(0)
        else:
            print(key[a]+1)

if __name__ == "__main__":
    main()