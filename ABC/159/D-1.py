from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    ans = 0
    for i, j in d.items():
        ans += j * (j - 1) // 2

    for a in A:
        tmp = ans - (d[a] * (d[a] - 1) // 2)
        tmp += ((d[a] - 1) * (d[a] - 2) // 2)
        print(tmp)



if __name__ == "__main__":
    main()