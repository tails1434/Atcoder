from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    total = 0
    for i, j in d.items():
        total += (j * (j - 1)) // 2

    for a in A:
        print(total - (d[a] - 1))



if __name__ == "__main__":
    main()