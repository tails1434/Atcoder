def main():
    x, y = map(int, input().split())
    k = int(input())
    if y >= k:
        print(x + k)
    elif x + y >= k:
        print(y + x + y - k)
    else:
        print(y)


if __name__ == "__main__":
    main()