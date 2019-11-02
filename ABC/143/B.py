import itertools

def main():
    N = int(input())
    d = list(map(int, input().split()))

    ans = 0

    for i, j in list(itertools.combinations(d,2)):
        ans += i * j

    print(ans)

if __name__ == "__main__":
    main()