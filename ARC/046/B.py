def main():
    N = int(input())
    A, B = map(int, input().split())
    if A >= N:
        print('Takahashi')
        exit()

    if A == B:
        if N % (A + 1) == 0:
            print('Aoki')
        else:
            print('Takahashi')
        exit()

    if A > B:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == "__main__":
    main()