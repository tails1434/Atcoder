def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    flag = True
    for a in A:
        if a % 2 == 1:
            flag = False
            break
            
    if flag:
        print('second')
    else:
        print('first')


if __name__ == "__main__":
    main()