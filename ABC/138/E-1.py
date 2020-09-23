from collections import defaultdict
from bisect import bisect_right

def main():
    S = input()
    T = input()
    Ls = len(S)
    Lt = len(T)
    d = defaultdict(list)
    for i in range(Ls):
        d[S[i]].append(i+1)

    now = 0
    ans = 0
    for i in range(Lt):
        if not d[T[i]]:
            print(-1)
            exit()
        ni = bisect_right(d[T[i]], now)
        if ni >= len(d[T[i]]):
            now = 0
            ans += Ls
            ni = bisect_right(d[T[i]], now)
            now = d[T[i]][ni]
        else:
            now = d[T[i]][ni]

    ans += now
    print(ans)


if __name__ == "__main__":
    main()