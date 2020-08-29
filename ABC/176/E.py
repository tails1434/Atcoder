from collections import defaultdict
import sys

input = sys.stdin.readline

def main():
    H, W, M = map(int, input().split())
    d = defaultdict(int)
    e = defaultdict(int)
    x = defaultdict(set)
    y = defaultdict(set)
    X = []
    for _ in range(M):
        h, w = map(int, input().split())
        d[h] += 1
        e[w] += 1
        x[h].add(w)
        y[w].add(h)
        
    a = max(d.values())
    b = max(e.values())
    cand_d = set()
    cand_e = set()
    for i, j in d.items():
        if j == a:
            cand_d.add(i)

    for i, j in e.items():
        if j == b:
            cand_e.add(i)

    for i in cand_d:
        if (cand_e - x[i]) != set():
            ans = a + b
            print(ans)
            exit()

    for i in cand_e:
        if (cand_d - y[i]) != set():
            ans = a + b
            print(ans)
            exit()

    print(a + b - 1)


if __name__ == "__main__":
    main()