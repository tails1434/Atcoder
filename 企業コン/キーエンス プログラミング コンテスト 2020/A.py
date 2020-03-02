def main():
    H = int(input())
    W = int(input())
    N = int(input())
    ans = N // max(H, W) if N % max(H, W) == 0 else N // max(H, W) + 1
    print(ans)


if __name__ == "__main__":
    main()