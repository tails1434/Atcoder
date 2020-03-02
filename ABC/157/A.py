def main():
    N = int(input())
    ans = N // 2 if N % 2 == 0 else (N // 2) + 1
    print(ans)


if __name__ == "__main__":
    main()