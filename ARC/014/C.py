from collections import defaultdict

def main():
    N = int(input())
    S = input()
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    ans = 0
    for i, j in d.items():
        if j % 2 == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()