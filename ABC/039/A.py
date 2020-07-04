def main():
    A, B, C = map(int, input().split())
    ans = 2 * A * B + 2 * B * C + 2 * C * A
    print(ans)


if __name__ == "__main__":
    main()