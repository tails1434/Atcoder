def main():
    A, B = map(int, input().split())

    if A - 2 * B <= 0:
        print(0)
    else:
        print(A - 2 * B)

if __name__ == "__main__":
    main()