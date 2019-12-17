def main():
    N = int(input())
    for x in range(50001):
        if int(x * 1.08) == N:
            print(x)
            exit()

    print(':(')


if __name__ == "__main__":
    main()