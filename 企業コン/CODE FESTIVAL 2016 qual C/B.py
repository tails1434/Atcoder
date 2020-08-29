def main():
    K, T = map(int, input().split())
    A = list(map(int, input().split()))
    ans = max(A) - (sum(A) - max(A) + 1)
    print(max(0,ans))


if __name__ == "__main__":
    main()