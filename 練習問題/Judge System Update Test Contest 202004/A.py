def main():
    S, L, R = map(int, input().split())
    if L >= S:
        print(L)
    elif S >= R:
        print(R)
    else:
        print(S)


if __name__ == "__main__":
    main()