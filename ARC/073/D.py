from collections import defaultdict

def main():
    N, W = map(int, input().split())
    d = defaultdict(list)
    w1 = 0
    for i in range(N):
        w, v = map(int, input().split())
        if i == 0:
            w1 = w
        d[w].append(v)

    ans = 0
    d[w1].sort(reverse=True)
    d[w1 + 1].sort(reverse=True)
    d[w1 + 2].sort(reverse=True)
    d[w1 + 3].sort(reverse=True)

    for i in range(len(d[w1])+1):
        for j in range(len(d[w1+1])+1):
            for k in range(len(d[w1+2])+1):
                for l in range(len(d[w1+3])+1):
                    tmp = sum(d[w1][:i]) + sum(d[w1+1][:j]) + sum(d[w1+2][:k]) + sum(d[w1+3][:l])

                    if w1 * i + (w1+1) * j + (w1+2) * k + (w1+3) * l <= W:
                        ans = max(ans,tmp)

    print(ans)


if __name__ == "__main__":
    main()