def main():
    M, D = map(int, input().split())

    if D < 20:
        print(0)
        exit()

    cnt = 0
    for i in range(1, M+1):
        for j in range(20,D+1):
            if i == int(str(j)[0]) * int(str(j)[1]):
                if int(str(j)[0]) >= 2 and int(str(j)[1]) >= 2:
                    cnt += 1

    print(cnt)
            


main()