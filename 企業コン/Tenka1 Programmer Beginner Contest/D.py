from itertools import combinations

def main():
    N = int(input())
    k = 0
    for i in range(N+5):
        if i * (i - 1) == 2 * N:
            k = i
            break
    if k == 0:
        print('No')
        exit()
    num = 0
    groups = [[] for _ in range(k)]
    for pattern in combinations(range(k), r=2):
        num += 1
        a, b = pattern
        groups[a].append(num)
        groups[b].append(num)
    print('Yes')
    print(k)
    for g in groups:
        print(len(g), end=" ")
        print(*g, sep=' ')


if __name__ == "__main__":
    main()