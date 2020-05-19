def main():
    K = int(input())
    S = input()
    len_S = len(S)
    if K >= len_S:
        print(S)
    else:
        print(S[:K] + '...')


if __name__ == "__main__":
    main()