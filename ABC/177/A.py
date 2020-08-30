def main():
    D, T, S = map(int, input().split())
    cnt = 0
    if D % S == 0:
        cnt = D // S
    else:
        cnt = D // S
        cnt += 1

    if cnt <= T:
        print('Yes')
    else:
        print('No')



if __name__ == "__main__":
    main()