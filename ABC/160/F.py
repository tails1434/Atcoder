def main():
    N = int(input())
    d = [[0] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d[a].append(b)
        d[b].append(a)

    MOD = 10 ** 9 + 7
    




if __name__ == "__main__":
    main()