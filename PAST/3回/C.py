def main():
    A, R, N = map(int, input().split())
    if R == 1:
        print(A)
        exit()
    check_num = 10 ** 9
    cnt = 1
    tmp = A
    while True:
        if tmp > 10 ** 9:
            print('large')
            exit()
        if cnt >= N:
            break
        tmp *= R
        cnt += 1
    print(tmp)





if __name__ == "__main__":
    main()