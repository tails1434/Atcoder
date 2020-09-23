def main():
    N = int(input())
    cnt = 0
    flag = False
    for _ in range(N):
        D1, D2 = map(int, input().split())
        if D1 == D2:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            flag = True
    if flag:
        print('Yes')
    else:
        print('No')



if __name__ == "__main__":
    main()