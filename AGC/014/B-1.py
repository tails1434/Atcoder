from collections import defaultdict
def main():
    N, M = map(int, input().split())
    d = defaultdict(int)
    for _ in range(M):
        a, b = map(int, input().split())
        d[a] += 1
        d[b] += 1

    for i, j in d.items():
        if j % 2 == 1:
            print('NO')
            exit()

    print('YES')


if __name__ == "__main__":
    main()