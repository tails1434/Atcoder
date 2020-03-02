def main():
    N = int(input())
    A = list(map(int, input().split()))
    flag = True
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                continue
            else:
                flag = False

    if flag:
        print('APPROVED')
    else:
        print('DENIED')


if __name__ == "__main__":
    main()