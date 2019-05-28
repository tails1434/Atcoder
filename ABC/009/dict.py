from collections import Counter
N, K = map(int, input().split())
S = list(input())
sorted_s = sorted(S)
T = ""

diff = 0
for i in range(N):
    c = Counter(S[:i+1]) - Counter(T)
    print(c)
    for s in sorted_s:
        diff1 = diff + (s != S[i])
        print(diff1)
        diff2 = sum(c.values()) - (c[s]>0)
        if diff1 + diff2 <= K:
            T += s
            sorted_s.remove(s)
            diff = diff1
            break

print(T)