def main():
    a, b, c, d = map(int, input().split())
    ans = a * c
    ans = max(ans, a * d)
    ans = max(ans, b * c)
    ans = max(ans, b * d)
    print(ans)


if __name__ == "__main__":
    main()